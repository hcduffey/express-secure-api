from rest_framework import serializers
from main_app.vulnerabilities.models import Vulnerability

class VulnerabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vulnerability
        fields = ["id", "type", "category", "file", "match_line", "description", "severity"]