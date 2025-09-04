from django.shortcuts import render, get_object_or_404
from .models import Blog

def list_blogs(request):
    posts = Blog.objects.order_by('-created_at')
    return render(request, "blogs/list.html", {"posts": posts})

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, "blogs/detail.html", {"post": post})
