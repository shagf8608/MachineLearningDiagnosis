# Generated by Django 3.2.12 on 2024-04-21 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mldiagno', '0005_remove_new_patient_outcome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_patient',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='blood_pressure',
            new_name='BloodPressure',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='dp_function',
            new_name='DiabetesPedigreeFunction',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='glucose_level',
            new_name='Glucose',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='insulin_level',
            new_name='Insulin',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='patient_id',
            new_name='Patient_ID',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='num_pregnancies',
            new_name='Pregnancies',
        ),
        migrations.RenameField(
            model_name='new_patient',
            old_name='skin_thickness',
            new_name='SkinThickness',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='blood_pressure',
            new_name='BloodPressure',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='dp_function',
            new_name='DiabetesPedigreeFunction',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='glucose_level',
            new_name='Glucose',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='insulin_level',
            new_name='Insulin',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='patient_id',
            new_name='Patient_ID',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='num_pregnancies',
            new_name='Pregnancies',
        ),
        migrations.RenameField(
            model_name='referdata',
            old_name='skin_thickness',
            new_name='SkinThickness',
        ),
    ]