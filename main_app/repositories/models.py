from django.db import models
from main_app.githubaccounts.models import GitHubAccount

# Create your models here.

class Repository(models.Model):
    url = models.CharField(max_length=200, blank=False)
    githubaccount = models.ForeignKey(GitHubAccount, related_name="repositories", on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['url']

