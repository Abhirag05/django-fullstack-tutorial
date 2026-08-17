from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"path: {request.path} - {datetime.now()}.")

    def process_response(self, request, response):
        print(f"Response is being processed at {datetime.now()} and status: {response.status_code}.")
        return response

class BlockIpMiddleware(MiddlewareMixin):
    BLOCKED_IPS = ['']  # Example blocked IPs

    def process_request(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        if client_ip in self.BLOCKED_IPS:
            return HttpResponse("Access Denied", status=403)
        return None