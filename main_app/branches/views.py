from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main_app.branches.models import Branch
from main_app.branches.serializers import BranchSerializer

# Create your views here.

# Branch Views

@csrf_exempt
def branch_list(request):
    """
    List all branches, or create a new branch.
    """
    if request.method == 'GET':
        branchlist = Branch.objects.all()
        serializer = BranchSerializer(branchlist, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BranchSerializer(data=data, context={'request': request, 'repository': data['repository']})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def branch_detail(request, pk):
    """
    Retrieve, update or delete a branch.
    """
    try:
        branch = Branch.objects.get(pk=pk)
    except Branch.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BranchSerializer(branch, context={'request': request})
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BranchSerializer(branch, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        branch.delete()
        return HttpResponse(status=204)