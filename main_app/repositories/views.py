from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main_app.repositories.models import Repository
from main_app.repositories.serializers import RepositorySerializer
import requests

# Create your views here.
@csrf_exempt
def repository_list(request):
    """
    List all repositories, or create a new repository.
    """
    if request.method == 'GET':
        repositorylist = Repository.objects.all()
        serializer = RepositorySerializer(repositorylist, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = RepositorySerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def repository_detail(request, pk):
    """
    Retrieve, update or delete a repository.
    """
    try:
        repository = Repository.objects.get(pk=pk)
    except Repository.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RepositorySerializer(repository, context={'request': request})
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        github_api = f'{data["url"]}/branches'
        api_response = requests.get(github_api)
        json_response = api_response.json()
        
        branches = []
        for response in json_response:
            branches.append({
                    "url": f'https://www.github.com/{response["full_name"]}'},
            )
            
        data["repositories"] = repos


        serializer = RepositorySerializer(repository, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        repository.delete()
        return HttpResponse(status=204)