from django.db import models
from main_app.scans.models import Scan

# Create your models here.

class Vulnerability(models.Model):
    type = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)
    file = models.CharField(max_length=100, blank=False)
    match_line = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)

    severity = models.CharField(max_length=100, blank=False)

    scan = models.ForeignKey(Scan, related_name="vulnerabilities", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description
        
    class Meta:
        ordering = ['severity']

