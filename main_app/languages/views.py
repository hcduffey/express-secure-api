from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main_app.languages.models import Language
from main_app.languages.serializers import LanguageSerializer

# Create your views here.

# Language Views

@csrf_exempt
def language_list(request):
    """
    List all code languages, or create a new language.
    """
    if request.method == 'GET':
        languagelist = Language.objects.all()
        serializer = LanguageSerializer(languagelist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def language_detail(request, pk):
    """
    Retrieve, update or delete a code language.
    """
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(language, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        language.delete()
        return HttpResponse(status=204)

