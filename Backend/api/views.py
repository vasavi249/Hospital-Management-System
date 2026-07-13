import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Doctor, Appointment, MedicalRecord, Bill

def parse_body(request):
    try:
        return json.loads(request.body)
    except:
        return {}

# ----------------- PATIENT APIs -----------------
@csrf_exempt
def add_patient(request):
    if request.method == 'POST':
        data = parse_body(request)
        patient = Patient.objects.create(**data)
        return JsonResponse({'message': 'Patient added', 'id': patient.patient_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_patients(request):
    if request.method == 'GET':
        patients = list(Patient.objects.values())
        return JsonResponse(patients, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_patient(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Patient.objects.filter(patient_id=id).update(**data)
        return JsonResponse({'message': 'Patient updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_patient(request, id):
    if request.method == 'DELETE':
        Patient.objects.filter(patient_id=id).delete()
        return JsonResponse({'message': 'Patient deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

# ----------------- DOCTOR APIs -----------------
@csrf_exempt
def add_doctor(request):
    if request.method == 'POST':
        data = parse_body(request)
        doctor = Doctor.objects.create(**data)
        return JsonResponse({'message': 'Doctor added', 'id': doctor.doctor_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_doctors(request):
    if request.method == 'GET':
        doctors = list(Doctor.objects.values())
        return JsonResponse(doctors, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_doctor(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Doctor.objects.filter(doctor_id=id).update(**data)
        return JsonResponse({'message': 'Doctor updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_doctor(request, id):
    if request.method == 'DELETE':
        Doctor.objects.filter(doctor_id=id).delete()
        return JsonResponse({'message': 'Doctor deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

# ----------------- APPOINTMENT APIs -----------------
@csrf_exempt
def add_appointment(request):
    if request.method == 'POST':
        data = parse_body(request)
        appointment = Appointment.objects.create(**data)
        return JsonResponse({'message': 'Appointment added', 'id': appointment.appointment_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_appointments(request):
    if request.method == 'GET':
        appointments = list(Appointment.objects.values())
        return JsonResponse(appointments, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_appointment(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Appointment.objects.filter(appointment_id=id).update(**data)
        return JsonResponse({'message': 'Appointment updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_appointment(request, id):
    if request.method == 'DELETE':
        Appointment.objects.filter(appointment_id=id).delete()
        return JsonResponse({'message': 'Appointment deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

# ----------------- MEDICAL RECORD APIs -----------------
@csrf_exempt
def add_record(request):
    if request.method == 'POST':
        data = parse_body(request)
        record = MedicalRecord.objects.create(**data)
        return JsonResponse({'message': 'Record added', 'id': record.record_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_records(request):
    if request.method == 'GET':
        records = list(MedicalRecord.objects.values())
        return JsonResponse(records, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_record(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        MedicalRecord.objects.filter(record_id=id).update(**data)
        return JsonResponse({'message': 'Record updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_record(request, id):
    if request.method == 'DELETE':
        MedicalRecord.objects.filter(record_id=id).delete()
        return JsonResponse({'message': 'Record deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

# ----------------- BILLING APIs -----------------
@csrf_exempt
def add_bill(request):
    if request.method == 'POST':
        data = parse_body(request)
        bill = Bill.objects.create(**data)
        return JsonResponse({'message': 'Bill added', 'id': bill.bill_id})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def get_bills(request):
    if request.method == 'GET':
        bills = list(Bill.objects.values())
        return JsonResponse(bills, safe=False)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def update_bill(request, id):
    if request.method == 'PUT':
        data = parse_body(request)
        Bill.objects.filter(bill_id=id).update(**data)
        return JsonResponse({'message': 'Bill updated'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def delete_bill(request, id):
    if request.method == 'DELETE':
        Bill.objects.filter(bill_id=id).delete()
        return JsonResponse({'message': 'Bill deleted'})
    return JsonResponse({'error': 'Invalid method'}, status=405)
