from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'patient_id',
            'name',
            'date_of_birth',
            'age',
            'gender',
            'phone',
            'blood_group',
            'emergency_contact',
            'medical_history',
        ]