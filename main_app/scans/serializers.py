from rest_framework import serializers
from main_app.scans.models import Scan
from main_app.branches.models import Branch
import requests
from datetime import datetime
import zipfile
from njsscan.njsscan import NJSScan

# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url):
    local_filename = "tmp/"
    local_filename += url.split('/')[-3]
    local_filename += "-"
    local_filename += url.split('/')[-1]
    local_filename += "-"
    local_filename += str(datetime.now())
    local_filename += ".zip"

    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

class ScanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scan
        fields = ["id", "name"]

    def create(self, validated_data):
        branch = Branch.objects.get(pk=self.context['branch_id'])
        branch_url = branch.name
        github_api = branch_url.replace("branches", "zipball")
        filename = download_file(github_api)

        node_source = "tmp/"
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('tmp')
            node_source += zip_ref.filelist[0].filename

        print(node_source)
        scanner = NJSScan([node_source], json=True, check_controls=False)
        scanner.scan()

        print(scanner.result)

        new_scan = Scan.objects.create(**validated_data)
        return new_scan

class ScanSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = Scan
        fields = ["id", "name", "vulnerabilities", "date"]