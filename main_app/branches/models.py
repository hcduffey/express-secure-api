from django.db import models
from main_app.repositories.models import Repository

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=100, blank=False)
    repository = models.ForeignKey(Repository, related_name="branches", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

