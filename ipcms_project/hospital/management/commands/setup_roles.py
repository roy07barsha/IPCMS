from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):

    help = "Create IPCMS RBAC roles and assign permissions"


    def handle(self, *args, **options):

        # ADMIN
        

        admin_group, _ = Group.objects.get_or_create(
            name="IPCMS Admin"
        )

        admin_permissions = Permission.objects.filter(
            content_type__app_label="hospital"
        )

        admin_group.permissions.set(
            admin_permissions
        )


        # ====================================================
        # DOCTOR
        # ====================================================

        doctor_group, _ = Group.objects.get_or_create(
            name="Doctor"
        )

        doctor_permissions = [
            "view_patient",
            "view_doctor",
            "view_appointment",
            "view_consultation",
            "add_consultation",
            "change_consultation",
            "view_prescription",
            "add_prescription",
            "change_prescription",
        ]

        doctor_group.permissions.set(
            Permission.objects.filter(
                content_type__app_label="hospital",
                codename__in=doctor_permissions
            )
        )


        # ====================================================
        # RECEPTIONIST
        # ====================================================

        receptionist_group, _ = Group.objects.get_or_create(
            name="Receptionist"
        )

        receptionist_permissions = [
            "view_patient",
            "add_patient",
            "change_patient",

            "view_doctor",

            "view_appointment",
            "add_appointment",
            "change_appointment",

            "view_consultation",

            "view_prescription",
        ]

        receptionist_group.permissions.set(
            Permission.objects.filter(
                content_type__app_label="hospital",
                codename__in=receptionist_permissions
            )
        )


        self.stdout.write(
            self.style.SUCCESS(
                "IPCMS RBAC roles created successfully."
            )
        )

        self.stdout.write(
            "Created roles:"
        )

        self.stdout.write(
            " - IPCMS Admin"
        )

        self.stdout.write(
            " - Doctor"
        )

        self.stdout.write(
            " - Receptionist"
        )