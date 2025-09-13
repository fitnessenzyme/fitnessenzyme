from django.shortcuts import render
from blogs.models import Blog   # import Blog model from blogs app

def home(request):
    latest_posts = Blog.objects.order_by('-created_at')[:3]
    return render(request, "base.html", {"latest_posts": latest_posts})






# from django.shortcuts import render

# def home(request):
#     return render(request, "base.html")  