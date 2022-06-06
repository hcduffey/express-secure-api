from rest_framework import serializers
from main_app.scans.models import Scan

class ScanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scan
        fields = ["id", "name", "vulnerabilities"]

class ScanSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = Scan
        fields = ["id", "name", "vulnerabilities", "date"]