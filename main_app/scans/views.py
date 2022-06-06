from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main_app.scans.models import Scan
from main_app.scans.serializers import ScanSerializer, ScanSerializerGet
import requests

# Create your views here.

# Scan Views

@csrf_exempt
def scan_list(request):
    """
    List all scan, or create a new scan.
    """
    if request.method == 'GET':
        scanlist = Scan.objects.all()
        serializer = ScanSerializer(scanlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScanSerializer(data=data, context={'request': request, 'branch_id': data['branch_id']})

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def scan_detail(request, pk):
    """
    Retrieve, update or delete a scan.
    """
    try:
        scan = Scan.objects.get(pk=pk)
    except Scan.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ScanSerializerGet(scan)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ScanSerializer(scan, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        scan.delete()
        return HttpResponse(status=204)

