import urllib.request
import urllib.error
import json

url = 'http://127.0.0.1:8000/patients/add/'
data = {
    "patient_name": "Test User",
    "age": "30",
    "gender": "Male",
    "phone": "1234567890",
    "email": "test@example.com",
    "blood_group": "A+",
    "address": "Test Address"
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        print("Status:", response.status)
        print("Response:", response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("HTTPError:", e.code, e.reason)
    print("Response:", e.read().decode('utf-8'))
except Exception as e:
    print("Exception:", str(e))
