from http.client import responses
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main_app.githubaccounts.models import GitHubAccount
from main_app.githubaccounts.serializers import GitHubAccountSerializer
import requests

# Create your views here.
@csrf_exempt
def github_account_list(request):
    """
    List all github accounts, or create a new account.
    """
    if request.method == 'GET':
        githubaccounts = GitHubAccount.objects.all()
        serializer = GitHubAccountSerializer(githubaccounts, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        
        github_api = f'https://api.github.com/users/{data["owner"]}/repos'
        api_response = requests.get(github_api)
        json_response = api_response.json()
        
        repos = []
        for response in json_response:
            repos.append({
                    "url": f'https://api.github.com/{response["full_name"]}'},
            )
            
        data["repositories"] = repos
        serializer = GitHubAccountSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def githubaccount_detail(request, pk):
    """
    Retrieve, update or delete a github account.
    """
    try:
        githubaccount = GitHubAccount.objects.get(pk=pk)
    except GitHubAccount.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GitHubAccountSerializer(githubaccount, context={'request': request})
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GitHubAccountSerializer(githubaccount, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        githubaccount.delete()
        return HttpResponse(status=204)