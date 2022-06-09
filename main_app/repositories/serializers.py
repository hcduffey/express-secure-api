from rest_framework import serializers
from main_app.repositories.models import Repository
from main_app.branches.models import Branch
from main_app.branches.serializers import BranchSerializer

class RepositorySerializer(serializers.ModelSerializer):

    languages = serializers.StringRelatedField(many=True, read_only=True)
    branches = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Repository
        fields = ["id", "url", "branches", "languages"]

    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        
        for branch_data in self.context['branches']:
            if(len(Branch.objects.all().filter(name=branch_data['name'])) == 0):
                Branch.objects.create(repository=instance, **branch_data)

        return instance
