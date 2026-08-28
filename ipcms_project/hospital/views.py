from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .models import AuditLog

from .models import (
    Patient,
    Doctor,
    Appointment,
    Consultation,
    Prescription,
)

from .forms import PatientForm

# REST API imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import PatientSerializer


# ============================================================
# DASHBOARD
# ============================================================

@login_required
def dashboard(request):

    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    total_consultations = Consultation.objects.count()
    total_prescriptions = Prescription.objects.count()

    scheduled_appointments = Appointment.objects.filter(
        status="Scheduled"
    ).count()

    completed_appointments = Appointment.objects.filter(
        status="Completed"
    ).count()

    cancelled_appointments = Appointment.objects.filter(
        status="Cancelled"
    ).count()

    upcoming_appointments = Appointment.objects.filter(
        status="Scheduled"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )[:5]

    return render(request, "hospital/dashboard.html", {
        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,
        "total_consultations": total_consultations,
        "total_prescriptions": total_prescriptions,

        "scheduled_appointments": scheduled_appointments,
        "completed_appointments": completed_appointments,
        "cancelled_appointments": cancelled_appointments,

        "upcoming_appointments": upcoming_appointments,
    })


# ============================================================
# PATIENT CRUD
# ============================================================

@login_required
@permission_required(
    'hospital.view_patient',
    raise_exception=True
)
def patient_list(request):

    patients = Patient.objects.all()

    context = {
        'patients': patients,
    }

    return render(
        request,
        'hospital/patients.html',
        context
    )


@login_required
@permission_required(
    'hospital.add_patient',
    raise_exception=True
)
def add_patient(request):

    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            patient = form.save()

            create_audit_log(
                request.user,
                'Created',
                'Patient',
                patient.id
            )

            return redirect('patient_list')

    else:
        form = PatientForm()

    return render(
        request,
        'hospital/patient_form.html',
        {
            'form': form
        }
    )


@login_required
@permission_required(
    'hospital.change_patient',
    raise_exception=True
)
def edit_patient(request, patient_id):

    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        form = PatientForm(
            request.POST,
            instance=patient
        )

        if form.is_valid():
            patient = form.save()

            create_audit_log(
                request.user,
                'Updated',
                'Patient',
                patient.id
            )

            return redirect('patient_list')

    else:
        form = PatientForm(
            instance=patient
        )

    return render(
        request,
        'hospital/patient_edit.html',
        {
            'form': form,
            'patient': patient
        }
    )


@login_required
@permission_required(
    'hospital.delete_patient',
    raise_exception=True
)
def delete_patient(request, patient_id):

    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':

        patient_id_value = patient.id

        patient.delete()

        create_audit_log(
            request.user,
            'Deleted',
            'Patient',
            patient_id_value
        )

        return redirect('patient_list')

    return render(
        request,
        'hospital/patient_delete.html',
        {
            'patient': patient
        }
    )


# ============================================================
# APPOINTMENT CRUD
# ============================================================

@login_required
@permission_required(
    'hospital.view_appointment',
    raise_exception=True
)
def appointment_list(request):

    appointments = Appointment.objects.all().select_related(
        'patient',
        'doctor'
    )

    return render(
        request,
        'hospital/appointments.html',
        {
            'appointments': appointments
        }
    )


@login_required
@permission_required(
    'hospital.add_appointment',
    raise_exception=True
)
def add_appointment(request):

    if request.method == 'POST':

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')

        appointment = Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        )

        create_audit_log(
            request.user,
            'Created',
            'Appointment',
            appointment.id
        )

        return redirect('appointment_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/appointments_form.html',
        {
            'patients': patients,
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.change_appointment',
    raise_exception=True
)
def edit_appointment(request, appointment_id):

    appointment = Appointment.objects.get(
        id=appointment_id
    )

    if request.method == 'POST':

        appointment.patient_id = request.POST.get(
            'patient'
        )

        appointment.doctor_id = request.POST.get(
            'doctor'
        )

        appointment.appointment_date = request.POST.get(
            'appointment_date'
        )

        appointment.appointment_time = request.POST.get(
            'appointment_time'
        )

        appointment.status = request.POST.get(
            'status'
        )

        appointment.save()

        create_audit_log(
            request.user,
            'Updated',
            'Appointment',
            appointment.id
        )

        return redirect('appointment_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/appointment_edit.html',
        {
            'appointment': appointment,
            'patients': patients,
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.delete_appointment',
    raise_exception=True
)
def delete_appointment(request, appointment_id):

    appointment = Appointment.objects.get(
        id=appointment_id
    )

    if request.method == 'POST':

        appointment_id_value = appointment.id

        appointment.delete()

        create_audit_log(
            request.user,
            'Deleted',
            'Appointment',
            appointment_id_value
        )

        return redirect('appointment_list')

    return render(
        request,
        'hospital/appointment_delete.html',
        {
            'appointment': appointment
        }
    )


# ============================================================
# CONSULTATION CRUD
# ============================================================

@login_required
@permission_required(
    'hospital.view_consultation',
    raise_exception=True
)
def consultation_list(request):

    consultations = Consultation.objects.all()

    return render(
        request,
        'hospital/consultations.html',
        {
            'consultations': consultations
        }
    )


@login_required
@permission_required(
    'hospital.add_consultation',
    raise_exception=True
)
def add_consultation(request):

    if request.method == 'POST':

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        symptoms = request.POST.get('symptoms')
        diagnosis = request.POST.get('diagnosis')
        treatment = request.POST.get('treatment')

        consultation = Consultation.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            symptoms=symptoms,
            diagnosis=diagnosis,
            treatment=treatment
        )

        create_audit_log(
            request.user,
            'Created',
            'Consultation',
            consultation.id
        )

        return redirect('consultation_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/consultations_form.html',
        {
            'patients': patients,
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.change_consultation',
    raise_exception=True
)
def edit_consultation(request, consultation_id):

    consultation = Consultation.objects.get(
        id=consultation_id
    )

    if request.method == 'POST':

        consultation.patient_id = request.POST.get(
            'patient'
        )

        consultation.doctor_id = request.POST.get(
            'doctor'
        )

        # Restored symptoms field
        consultation.symptoms = request.POST.get(
            'symptoms'
        )

        consultation.diagnosis = request.POST.get(
            'diagnosis'
        )

        consultation.treatment = request.POST.get(
            'treatment'
        )

        consultation.save()

        create_audit_log(
            request.user,
            'Updated',
            'Consultation',
            consultation.id
        )

        return redirect('consultation_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/consultation_edit.html',
        {
            'consultation': consultation,
            'patients': patients,
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.delete_consultation',
    raise_exception=True
)
def delete_consultation(request, consultation_id):

    consultation = Consultation.objects.get(
        id=consultation_id
    )

    if request.method == 'POST':

        consultation_id_value = consultation.id

        consultation.delete()

        create_audit_log(
            request.user,
            'Deleted',
            'Consultation',
            consultation_id_value
        )

        return redirect('consultation_list')

    return render(
        request,
        'hospital/consultation_delete.html',
        {
            'consultation': consultation
        }
    )


# ============================================================
# PRESCRIPTION CRUD
# ============================================================

@login_required
@permission_required(
    'hospital.view_prescription',
    raise_exception=True
)
def prescription_list(request):

    prescriptions = Prescription.objects.all()

    return render(
        request,
        'hospital/prescriptions.html',
        {
            'prescriptions': prescriptions
        }
    )


@login_required
@permission_required(
    'hospital.add_prescription',
    raise_exception=True
)
def add_prescription(request):

    if request.method == 'POST':

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        medicine = request.POST.get('medicine')
        dosage = request.POST.get('dosage')
        duration = request.POST.get('duration')

        prescription = Prescription.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            medicine=medicine,
            dosage=dosage,
            duration=duration
        )

        create_audit_log(
            request.user,
            'Created',
            'Prescription',
            prescription.id
        )

        return redirect('prescription_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/prescriptions_form.html',
        {
            'patients': patients,
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.change_prescription',
    raise_exception=True
)
def edit_prescription(request, prescription_id):

    prescription = Prescription.objects.get(
        id=prescription_id
    )

    if request.method == 'POST':

        prescription.patient_id = request.POST.get(
            'patient'
        )

        prescription.doctor_id = request.POST.get(
            'doctor'
        )

        prescription.medicine = request.POST.get(
            'medicine'
        )

        prescription.dosage = request.POST.get(
            'dosage'
        )

        prescription.duration = request.POST.get(
            'duration'
        )

        prescription.save()

        create_audit_log(
            request.user,
            'Updated',
            'Prescription',
            prescription.id
        )

        return redirect('prescription_list')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/prescription_edit.html',
        {
            'prescription': prescription,
            'patients': patients,
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.delete_prescription',
    raise_exception=True
)
def delete_prescription(request, prescription_id):

    prescription = Prescription.objects.get(
        id=prescription_id
    )

    if request.method == 'POST':

        prescription_id_value = prescription.id

        prescription.delete()

        create_audit_log(
            request.user,
            'Deleted',
            'Prescription',
            prescription_id_value
        )

        return redirect('prescription_list')

    return render(
        request,
        'hospital/prescription_delete.html',
        {
            'prescription': prescription
        }
    )


# ============================================================
# DOCTOR CRUD
# ============================================================

@login_required
@permission_required(
    'hospital.view_doctor',
    raise_exception=True
)
def doctor_list(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        'hospital/doctors.html',
        {
            'doctors': doctors
        }
    )


@login_required
@permission_required(
    'hospital.add_doctor',
    raise_exception=True
)
def add_doctor(request):

    if request.method == 'POST':

        user_id = request.POST.get('user')
        specialization = request.POST.get('specialization')
        phone = request.POST.get('phone')

        doctor = Doctor.objects.create(
            user_id=user_id,
            specialization=specialization,
            phone=phone
        )

        create_audit_log(
            request.user,
            'Created',
            'Doctor',
            doctor.id
        )

        return redirect('doctor_list')

    users = User.objects.all()

    return render(
        request,
        'hospital/doctor_form.html',
        {
            'users': users
        }
    )


@login_required
@permission_required(
    'hospital.change_doctor',
    raise_exception=True
)
def edit_doctor(request, doctor_id):

    doctor = Doctor.objects.get(
        id=doctor_id
    )

    if request.method == 'POST':

        doctor.specialization = request.POST.get(
            'specialization'
        )

        doctor.phone = request.POST.get(
            'phone'
        )

        doctor.save()

        create_audit_log(
            request.user,
            'Updated',
            'Doctor',
            doctor.id
        )

        return redirect('doctor_list')

    return render(
        request,
        'hospital/doctor_edit.html',
        {
            'doctor': doctor
        }
    )


@login_required
@permission_required(
    'hospital.delete_doctor',
    raise_exception=True
)
def delete_doctor(request, doctor_id):

    doctor = Doctor.objects.get(
        id=doctor_id
    )

    if request.method == 'POST':

        doctor_id_value = doctor.id

        doctor.delete()

        create_audit_log(
            request.user,
            'Deleted',
            'Doctor',
            doctor_id_value
        )

        return redirect('doctor_list')

    return render(
        request,
        'hospital/doctor_delete.html',
        {
            'doctor': doctor
        }
    )


# ============================================================
# REST API - PATIENT
# ============================================================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def patient_api(request):

    # GET permission
    if request.method == 'GET':

        if not request.user.has_perm(
            'hospital.view_patient'
        ):
            return Response(
                {
                    'detail':
                    'You do not have permission to view patients.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        patients = Patient.objects.all()

        serializer = PatientSerializer(
            patients,
            many=True
        )

        return Response(serializer.data)

    # POST permission
    if request.method == 'POST':

        if not request.user.has_perm(
            'hospital.add_patient'
        ):
            return Response(
                {
                    'detail':
                    'You do not have permission to add patients.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = PatientSerializer(
            data=request.data
        )

        if serializer.is_valid():

            patient = serializer.save()

            create_audit_log(
                request.user,
                'Created via API',
                'Patient',
                patient.id
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ============================================================
# REST API - PATIENT DETAIL
# ============================================================

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def patient_api_detail(request, patient_id):

    try:

        patient = Patient.objects.get(
            id=patient_id
        )

    except Patient.DoesNotExist:

        return Response(
            {
                'error': 'Patient not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

    # GET permission
    if request.method == 'GET':

        if not request.user.has_perm(
            'hospital.view_patient'
        ):
            return Response(
                {
                    'detail':
                    'You do not have permission to view patients.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = PatientSerializer(patient)

        return Response(serializer.data)

    # PUT permission
    elif request.method == 'PUT':

        if not request.user.has_perm(
            'hospital.change_patient'
        ):
            return Response(
                {
                    'detail':
                    'You do not have permission to change patients.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = PatientSerializer(
            patient,
            data=request.data
        )

        if serializer.is_valid():

            patient = serializer.save()

            create_audit_log(
                request.user,
                'Updated via API',
                'Patient',
                patient.id
            )

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE permission
    elif request.method == 'DELETE':

        if not request.user.has_perm(
            'hospital.delete_patient'
        ):
            return Response(
                {
                    'detail':
                    'You do not have permission to delete patients.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        patient_id_value = patient.id

        patient.delete()

        create_audit_log(
            request.user,
            'Deleted via API',
            'Patient',
            patient_id_value
        )

        return Response(
            {
                'message':
                'Patient deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )


# ============================================================
# AUDIT LOG HELPER
# ============================================================

def create_audit_log(user, action, model_name, object_id):

    AuditLog.objects.create(
        user=user,
        action=action,
        model_name=model_name,
        object_id=str(object_id)
    )