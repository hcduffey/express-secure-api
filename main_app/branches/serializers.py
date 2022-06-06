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

    # def create(self, validated_data):
    #     # get the repo name to generate the branch url
    #     # grab the branches and create them
    #     print(validated_data)
    #     # get the name of the associated repo to build the GitHub API request
    #     repository = Repository.objects.get(pk=self.context['repository'])

    #     # make the request to Github from the branches in the repo and save in JSON
    #     # github_api = f'{repository.url}/branches'
    #     # api_response = requests.get(github_api)
    #     # json_response = api_response.json()

    #     json_response = [{'name': 'master', 'commit': {'sha': '9e082b3d64a248f4e780a6e7ee2851ed45ada5a9', 'url': 'https://api.github.com/repos/hcduffey/calculatorjs/commits/9e082b3d64a248f4e780a6e7ee2851ed45ada5a9'}, 'protected': False}]
        
    #     # iterate through each of the returned branch names and add to the database

    #     validated_data["name"] = json_response[0]['name']
    #     branch = Branch.objects.create(**validated_data)
    #     branch.repository = repository
    #     branch.save()
            
    #     return branch