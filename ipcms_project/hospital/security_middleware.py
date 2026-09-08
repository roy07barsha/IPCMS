from .models import AuditLog


class SecurityMonitoringMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):

        response = self.get_response(request)

        # Monitor unauthorized and forbidden requests
        if response.status_code in [401, 403]:

            user = None

            if hasattr(request, "user"):
                if request.user.is_authenticated:
                    user = request.user

            AuditLog.objects.create(
                user=user,
                action=f"SECURITY EVENT HTTP {response.status_code}",
                model_name="Security",
                object_id=request.path[:50]
            )

        return response