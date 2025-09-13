# blogs/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

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
    content = CKEditor5Field('content', config_name='extends')
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

    @property
    def total_likes(self):
        return self.likes.count()


class Like(models.Model):
    blog = models.ForeignKey(Blog, related_name="likes", on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()  # since no login for visitors
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blog', 'ip_address')  # prevent multiple likes from same IP

    def __str__(self):
        return f"Like on {self.blog.title}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # visitor’s name
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"

