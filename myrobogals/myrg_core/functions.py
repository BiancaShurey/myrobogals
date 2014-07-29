from __future__ import unicode_literals
from future.builtins import *
import six


from .models import APILog

def log_api_call(request, request_body, role = None, note = None):    
    log_dict = {
        "user_role": role,
        "ip": get_client_ip(request),
        "api_url": request.get_full_path(),
        "api_body": request_body,
        "note": note,
    }
    
    new_log = APILog(**log_dict)
    
    try:
        new_log.save()
    except:
        return False
        
    return new_log

# http://stackoverflow.com/a/4581997
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip