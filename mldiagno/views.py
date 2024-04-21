import warnings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, PatientDataForm
from django.shortcuts import render
import os
from django.conf import settings
from sklearn.tree import DecisionTreeClassifier
from mldiagno.models import Referdata
import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def train_decision_tree_model():
    # Load the data from the Referdata model
    refer_data = Referdata.objects.all().values()
    df1 = pd.DataFrame(refer_data)
    if len(df1) < 1:
        warnings.warn("Train data cannot be empty")

    # Define features and target
    all_list = df1.columns.tolist()
    features = all_list[1:-1]
    target = all_list[-1]

    # Split features and target
    X = df1[features]
    y = df1[target]
    best_params = {'metric': 'manhattan', 'n_neighbors': 9, 'weights': 'distance'}
    # Train the decision tree model
    knn_clf = KNeighborsClassifier(**best_params)

    # Train the KNN classifier on the training data
    knn_clf.fit(X, y)
    return knn_clf


# login page
def dashboard(request):
    if request.method == 'POST':
        form = PatientDataForm(request.POST)
        if form.is_valid():
            dt_model = train_decision_tree_model()
            patient_data = form.cleaned_data
            patient_data.pop('Patient_ID', None)

            desired_order = ['Pregnancies', 'Glucose', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age',
                             'BloodPressure', 'SkinThickness']
            reorganized_dict = {key: patient_data[key] for key in desired_order}

            refer_data = Referdata.objects.all().values()
            df2 = pd.DataFrame(refer_data)
            all_list = df2.columns.tolist()
            columns1 = all_list[1:-1]
            df = pd.DataFrame([reorganized_dict])

            # Load the pre-trained model
            #base_directory = settings.BASE_DIR
            #model_path = os.path.join(base_directory, 'dt_model.joblib')
            #dt_model = joblib.load(model_path)
            pred_res = dt_model.predict(df)

            if pred_res[0] == 0:
                prediction = "Negative"
            else:
                prediction = "Positive"
            # Store prediction result in session
            request.session['prediction'] = prediction
            # Redirect to the result page
            return redirect('result')
    else:
        form = PatientDataForm()
    return render(request, 'dashboard.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('dashboard')  # Redirect to dashboard after successful login
            else:
                # Return an error message or render the login page again with an error
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def result(request):
    # Get prediction result from session
    prediction = request.session.get('prediction')
    return render(request, 'result.html', {'prediction': prediction})