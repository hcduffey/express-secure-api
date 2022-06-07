from rest_framework import serializers
from main_app.scans.models import Scan
from main_app.branches.models import Branch
from main_app.vulnerabilities.models import Vulnerability
from main_app.vulnerabilities.serializers import VulnerabilitySerializer
import requests
from datetime import datetime
import zipfile
from njsscan.njsscan import NJSScan
import os
import sys

PATH = os.environ['HOME']+'/tmp'

# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url):
 

    if os.path.exists(PATH):
        print("path exists")
        sys.stdout.flush()
    else:
        print("creating temp dir: " + PATH)
        sys.stdout.flush()
        os.makedirs(PATH)

    local_filename = PATH + "/"
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

    vulnerabilities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Scan
        fields = ["id", "name", "vulnerabilities"]

    def create(self, validated_data):
        # get the branch that the new scan will be associated with
        branch = Branch.objects.get(pk=self.context['branch_id'])

        # download the zip archive of the selected branch
        branch_url = branch.name
        github_api = branch_url.replace("branches", "zipball")
        filename = download_file(github_api)

        # extract the zip file
        node_source = PATH
        print(node_source)
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(PATH)
            node_source += "/" + zip_ref.filelist[0].filename
        print(node_source)
        #perform the scan of the unzipped files
        scanner = NJSScan([node_source], json=True, check_controls=False)
        scanner.scan()

        #create the scan record in the database
        new_scan = Scan.objects.create(branch=branch,**validated_data)

        #parse the scan results and store the vulnerabilties in the database
        for finding_type in scanner.result:

            for category in scanner.result.get(finding_type):
                if type(scanner.result.get(finding_type)) is list:
                    continue
                    
                for _ in scanner.result.get(finding_type).get(category):
                    description = scanner.result.get(finding_type).get(category)['metadata']['cwe']
                    severity = scanner.result.get(finding_type).get(category)['metadata']['severity']
                    files = scanner.result.get(finding_type).get(category)['files']
                    for file in files:
                        vulnerability = {
                            "type": finding_type,
                            "category": category,
                            "file": file["file_path"],
                            "match_line": file["match_lines"],
                            "description": description,
                            "severity": severity
                        }
                        # store the vulnerability in the database, associated with that scan
                        Vulnerability.objects.create(scan=new_scan, **vulnerability) # this is where the create happens
        
        return new_scan

class ScanSerializerGet(serializers.ModelSerializer):
    vulnerabilities = VulnerabilitySerializer(many=True)

    class Meta:
        model = Scan
        fields = ["id", "name", "vulnerabilities", "date", "branch"]