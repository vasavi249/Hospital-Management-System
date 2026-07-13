import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.management import call_command
from api.models import Patient, Doctor, Appointment, MedicalRecord, Bill

def seed():
    print("Running migrations...")
    call_command('makemigrations', 'api')
    call_command('migrate')

    print("Adding sample testing data...")
    # Patient
    Patient.objects.get_or_create(
        patient_id=101,
        defaults={
            "patient_name": "Rahul Sharma",
            "age": 28,
            "gender": "Male",
            "phone": "9876543210",
            "email": "rahul@gmail.com",
            "blood_group": "O+",
            "address": "Hyderabad"
        }
    )

    # Doctor
    Doctor.objects.get_or_create(
        doctor_id=201,
        defaults={
            "doctor_name": "Dr. Priya Reddy",
            "specialization": "Cardiologist",
            "department": "Cardiology",
            "experience": 10,
            "phone": "9988776655",
            "consultation_fee": 800
        }
    )

    # Appointment
    Appointment.objects.get_or_create(
        appointment_id=301,
        defaults={
            "patient_name": "Rahul Sharma",
            "doctor_name": "Dr. Priya Reddy",
            "appointment_date": "2026-07-20",
            "appointment_time": "10:30",
            "appointment_status": "Scheduled"
        }
    )

    # Medical Record
    MedicalRecord.objects.get_or_create(
        record_id=401,
        defaults={
            "patient_name": "Rahul Sharma",
            "doctor_name": "Dr. Priya Reddy",
            "diagnosis": "High Blood Pressure",
            "prescription": "Tablet A - Once Daily",
            "treatment": "Regular Monitoring",
            "visit_date": "2026-07-20"
        }
    )

    # Bill
    Bill.objects.get_or_create(
        bill_id=501,
        defaults={
            "patient_name": "Rahul Sharma",
            "consultation_fee": 800,
            "medicine_charge": 1200,
            "laboratory_charge": 500,
            "total_amount": 2500,
            "payment_method": "UPI",
            "payment_status": "Paid"
        }
    )
    print("Sample data added successfully! You can now check the frontend.")

if __name__ == '__main__':
    seed()
