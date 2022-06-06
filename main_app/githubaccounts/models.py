from django.db import models

# Create your models here.

class GitHubAccount(models.Model):
    owner = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['owner']

