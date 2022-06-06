from rest_framework import serializers
from main_app.languages.models import Language

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ["id", "name"]