from rest_framework import serializers
from main_app.repositories.models import Repository
from main_app.branches.models import Branch

class RepositorySerializer(serializers.HyperlinkedModelSerializer):

    languages = serializers.StringRelatedField(many=True, read_only=True)
    branches = serializers.HyperlinkedRelatedField(view_name="branch_detail", read_only=True, many=True)

    class Meta:
        model = Repository
        fields = ["id", "url", "branches", "languages"]

    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        
        print(self.context['branches'])
        print(instance)
        for branch_data in self.context['branches']:
            Branch.objects.create(repository=instance, **branch_data)

        return instance
