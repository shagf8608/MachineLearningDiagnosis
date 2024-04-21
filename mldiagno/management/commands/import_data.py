# import_data.py
# import_data.py

import os
from django.core.management.base import BaseCommand
import pandas as pd
from mldiagno.models import Referdata

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        file_path = os.path.join(base_dir, 'diabetes.csv')

        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            # Create a Referdata object with automatically generated patient_id
            refer_data = Referdata.objects.create(
                Pregnancies = row['Pregnancies'],
                Glucose = row['Glucose'],
                Insulin = row['Insulin'],
                BMI = row['BMI'],
                Age = row['Age'],
                DiabetesPedigreeFunction = row["DiabetesPedigreeFunction"],
                BloodPressure = row['BloodPressure'],
                SkinThickness = row['SkinThickness'],
                Outcome = row["Outcome"]
            )

            # Display the patient_id of the created Referdata object
            self.stdout.write(self.style.SUCCESS(f'Patient ID: {refer_data.Patient_ID}'))

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
