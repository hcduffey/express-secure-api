from rest_framework import serializers
from main_app.githubaccounts.models import GitHubAccount
from main_app.repositories.models import Repository
from main_app.repositories.serializers import RepositorySerializer

class GitHubAccountSerializer(serializers.ModelSerializer):

    repositories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = GitHubAccount
        fields = ["id", "owner", "repositories"]

    def create(self, validated_data):
        repositories_data = self.context['repositories']
        github_account = GitHubAccount.objects.create(**validated_data)
        for repository_data in repositories_data:
            Repository.objects.create(githubaccount=github_account, **repository_data)

        return github_account
