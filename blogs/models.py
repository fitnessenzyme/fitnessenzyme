from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Blog(models.Model):
    POST_TYPE_CHOICES = [
        ('text', 'Text Blog'),
        ('image', 'Image Blog'),
        ('video', 'Video Blog'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='text')

    content = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='blog_videos/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
