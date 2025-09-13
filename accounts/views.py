from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blogs.models import Blog  

def login_view(request):
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def dashboard(request):
    # return render(request, "accounts/dashboard.html")
    # def dashboard(request):
    # Fetch only blogs by the logged-in coach
    # user_blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
    # return render(request, "accounts/dashboard.html", {"user_blogs": user_blogs})
    blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "accounts/dashboard.html", {"blogs": blogs})



# accounts/views.py



from blogs.models import Blog, Like, Comment

@login_required(login_url="login")
def dashboard(request):
    blogs = Blog.objects.filter(author=request.user).order_by('-created_at')

    total_likes = Like.objects.filter(blog__in=blogs).count()
    total_comments = Comment.objects.filter(blog__in=blogs).count()

    # all comments for coach’s blogs
    comments = Comment.objects.filter(blog__in=blogs).order_by('-created_at')

    return render(request, "accounts/dashboard.html", {
        "blogs": blogs,
        "total_likes": total_likes,
        "total_comments": total_comments,
        "comments": comments,
    })


from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse

@login_required(login_url="login")
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Only allow if the logged-in coach owns the blog
    if comment.blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    comment.delete()
    return redirect(reverse("dashboard"))
