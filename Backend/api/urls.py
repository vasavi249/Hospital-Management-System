from django.urls import path
from . import views

urlpatterns = [
    path('patients/add/', views.add_patient),
    path('patients/', views.get_patients),
    path('patients/update/<int:id>/', views.update_patient),
    path('patients/delete/<int:id>/', views.delete_patient),
    
    path('doctors/add/', views.add_doctor),
    path('doctors/', views.get_doctors),
    path('doctors/update/<int:id>/', views.update_doctor),
    path('doctors/delete/<int:id>/', views.delete_doctor),
    
    path('appointments/add/', views.add_appointment),
    path('appointments/', views.get_appointments),
    path('appointments/update/<int:id>/', views.update_appointment),
    path('appointments/delete/<int:id>/', views.delete_appointment),
    
    path('records/add/', views.add_record),
    path('records/', views.get_records),
    path('records/update/<int:id>/', views.update_record),
    path('records/delete/<int:id>/', views.delete_record),
    
    path('bills/add/', views.add_bill),
    path('bills/', views.get_bills),
    path('bills/update/<int:id>/', views.update_bill),
    path('bills/delete/<int:id>/', views.delete_bill),
]