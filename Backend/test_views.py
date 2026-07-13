import os
import sys
import json
import django
from django.test import RequestFactory

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.views import add_patient, get_patients

factory = RequestFactory()

# Test Add Patient
data = {
    "patient_name": "Test User",
    "age": "28",
    "gender": "Male",
    "phone": "9876543210",
    "email": "test@test.com",
    "blood_group": "O+",
    "address": "NY"
}
request = factory.post('/patients/add/', data=json.dumps(data), content_type='application/json')
response = add_patient(request)
print("POST Response status:", response.status_code)
print("POST Response content:", response.content)

# Test Get Patient
request = factory.get('/patients/')
response = get_patients(request)
print("GET Response status:", response.status_code)
print("GET Response content:", response.content)
