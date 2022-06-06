from django.db import models
from main_app.branches.models import Branch

# Create your models here.

class Scan(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    branch = models.ForeignKey(Branch, related_name="scans", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['date']

