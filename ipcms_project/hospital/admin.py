from django.contrib import admin
from .models import Doctor, Patient, Appointment, Receptionist,Consultation, Prescription
from .models import AuditLog 

admin.site.register(Doctor)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'name', 'phone')
    search_fields = ('patient_id', 'name')
    
admin.site.register(Appointment)
admin.site.register(Receptionist)
admin.site.register(Consultation)
admin.site.register(Prescription)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'action',
        'model_name',
        'object_id',
        'timestamp',
    )

    list_filter = (
        'action',
        'model_name',
        'timestamp',
    )

    search_fields = (
        'user__username',
        'action',
        'model_name',
        'object_id',
    )