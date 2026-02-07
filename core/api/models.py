import secrets
from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class RefreshToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    token = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    revoked = models.BooleanField(default=False)

    @staticmethod
    def generate():
        return secrets.token_urlsafe(64)
    
    def is_valid(self):
        return not self.revoked and self.expires_at > timezone.now()
    
    def __str__(self):
        return f"{self.user} - {self.token}"