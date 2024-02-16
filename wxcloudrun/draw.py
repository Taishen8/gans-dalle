import xml.etree.ElementTree as ET
from django.http import JsonResponse


def get_drawn(request):
    body = ET.fromstring(request.body)
    return JsonResponse({"code": -1, "data": str(body)})
