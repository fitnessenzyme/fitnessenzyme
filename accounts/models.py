from django.db import models
from django.contrib.auth.models import User



class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.display_name or self.user.username