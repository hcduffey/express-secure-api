from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main_app.vulnerabilities.models import Vulnerability
from main_app.vulnerabilities.serializers import VulnerabilitySerializer

# Create your views here.

# Vulnerability Views

@csrf_exempt
def vulnerability_list(request):
    """
    List all scan, or create a new vulnerability.
    """
    if request.method == 'GET':
        vulnerabilitylist = Vulnerability.objects.all()
        serializer = VulnerabilitySerializer(vulnerabilitylist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VulnerabilitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def vulnerability_detail(request, pk):
    """
    Retrieve, update or delete a vulnerability.
    """
    try:
        scan = Vulnerability.objects.get(pk=pk)
    except Vulnerability.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VulnerabilitySerializer(scan)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VulnerabilitySerializer(scan, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        scan.delete()
        return HttpResponse(status=204)

