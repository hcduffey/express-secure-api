from django.db import models
from main_app.repositories.models import Repository

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100, blank=False, default="None")
    repository = models.ForeignKey(Repository, related_name="languages", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

