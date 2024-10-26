from django.db import models
from django.utils import timezone


class URLShortener(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=500)
    short_code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"
