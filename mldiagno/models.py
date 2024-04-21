from django.db import models

# Create your models here.
from django.db import models

class Referdata(models.Model):
    Patient_ID = models.BigAutoField(primary_key=True)
    Pregnancies = models.IntegerField()
    Glucose = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()
    Outcome = models.IntegerField()

    def __str__(self):
        return str(self.patient_id)

class New_patient(models.Model):
    Patient_ID = models.CharField(max_length=100, primary_key=True)
    Pregnancies = models.IntegerField()
    Glucose = models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    BloodPressure = models.FloatField()
    SkinThickness = models.FloatField()

    def __str__(self):
        return str(self.patient_id)