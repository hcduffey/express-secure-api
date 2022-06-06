from rest_framework import serializers
from main_app.branches.models import Branch
from main_app.githubaccounts.models import GitHubAccount
from main_app.repositories.models import Repository
import requests

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    scans = serializers.HyperlinkedRelatedField(view_name="scan_detail", read_only=True, many=True)

    class Meta:
        model = Branch
        fields = ["id", "name", "scans"]
