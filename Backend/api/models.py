from django.db import models

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    blood_group = models.CharField(max_length=5)
    address = models.TextField()

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    experience = models.IntegerField()
    phone = models.CharField(max_length=20)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    appointment_status = models.CharField(max_length=50)

class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    diagnosis = models.TextField()
    prescription = models.TextField()
    treatment = models.TextField()
    visit_date = models.DateField()

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=255)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_charge = models.DecimalField(max_digits=10, decimal_places=2)
    laboratory_charge = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
