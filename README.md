# Hospital Management System (HMS)

An efficient digital system to manage doctors, patients, appointments, medical records, and billing through a web application.

## Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6), Fetch API
- **Backend**: Django (Function-Based Views, REST APIs)
- **Database**: SQLite (default configuration)

---

## Installation & Setup

### Prerequisites
- Python 3.10+ installed.

### 1. Set Up Backend
Navigate to the `Backend` directory:
```bash
cd Backend
```

Create and activate a virtual environment (optional but recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations and seed the testing data:
```bash
python seed_db.py
```

Start the Django REST server:
```bash
python manage.py runserver
```
The backend server will run on `http://127.0.0.1:8000/`.

### 2. Set Up Frontend
Simply open the `Frontend/index.html` file in any modern web browser to access the application dashboard and management portals.

---

## Folder Structure
```text
HospitalManagementSystem/
│── Backend/
│     db.py
│     views.py
│     urls.py
│     manage.py
│     requirements.txt
│     seed_db.py
│     core/
│     api/
└── Frontend/
      index.html
      patients.html
      doctors.html
      appointments.html
      records.html
      billing.html
      dashboard.html
      style.css
      script.js
```

---

## API Endpoints (20 REST CRUD APIs)

### Patient Management
- `POST /patients/add/` - Register a patient
- `GET /patients/` - View all patients
- `PUT /patients/update/<id>/` - Update patient details
- `DELETE /patients/delete/<id>/` - Delete patient

### Doctor Management
- `POST /doctors/add/` - Add a doctor profile
- `GET /doctors/` - View all doctors
- `PUT /doctors/update/<id>/` - Update doctor profile
- `DELETE /doctors/delete/<id>/` - Delete doctor profile

### Appointment Management
- `POST /appointments/add/` - Book an appointment
- `GET /appointments/` - List all appointments
- `PUT /appointments/update/<id>/` - Update appointment details
- `DELETE /appointments/delete/<id>/` - Cancel/delete appointment

### Medical Record Management
- `POST /records/add/` - Add clinical medical record
- `GET /records/` - View all records
- `PUT /records/update/<id>/` - Update diagnosis/treatment
- `DELETE /records/delete/<id>/` - Delete medical record

### Billing Management
- `POST /bills/add/` - Generate invoice
- `GET /bills/` - View billing list
- `PUT /bills/update/<id>/` - Update payment status/method
- `DELETE /bills/delete/<id>/` - Delete bill record
