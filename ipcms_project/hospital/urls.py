from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<int:patient_id>/edit/', views.edit_patient, name='edit_patient'),
    path('patients/<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/<int:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),
    path('consultations/', views.consultation_list, name='consultation_list'),
    path('consultations/add/', views.add_consultation, name='add_consultation'),
    path('consultations/<int:consultation_id>/edit/', views.edit_consultation, name='edit_consultation'),
    path('consultations/<int:consultation_id>/delete/', views.delete_consultation, name='delete_consultation'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/add/', views.add_prescription, name='add_prescription'),
    path('prescriptions/<int:prescription_id>/edit/', views.edit_prescription, name='edit_prescription'),
    path('prescriptions/<int:prescription_id>/delete/', views.delete_prescription, name='delete_prescription'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/<int:doctor_id>/edit/', views.edit_doctor, name='edit_doctor'),
    path('doctors/<int:doctor_id>/delete/', views.delete_doctor, name='delete_doctor'),
    path('api/patients/', views.patient_api, name='patient_api'),
    path('api/patients/<int:patient_id>/', views.patient_api_detail, name='patient_api_detail'),
]