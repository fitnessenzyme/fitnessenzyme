from django.shortcuts import render, get_object_or_404
from .models import Blog

# def list_blogs(request):
#     posts = Blog.objects.order_by('-created_at')
#     return render(request, "blogs/list.html", {"posts": posts})

# def blog_detail(request, slug):
#     post = get_object_or_404(Blog, slug=slug)
#     return render(request, "blogs/detail.html", {"post": post})


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog
from .forms import BlogForm


# Show all blogs
class BlogListView(ListView):
    model = Blog
    template_name = "blogs/list.html"
    context_object_name = "posts"
    ordering = ['-created_at']

# Show single blog details
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/detail.html"
    context_object_name = "post"

# Create a new blog (Only coach)
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    # template_name = "blogs/blog_form.html"
    template_name = "blogs/blog_editor.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update an existing blog (Only coach)
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blogs/blog_editor.html"
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

# Delete a blog (Only coach)
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy('blog-list')

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author





# blogs/views.py
from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import Blog, Like, Comment
from .forms import BlogForm, CommentForm
from django.http import JsonResponse

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Handle Like
        if "like" in request.POST:
            ip = get_client_ip(request)
            like, created = Like.objects.get_or_create(blog=self.object, ip_address=ip)
            if not created:  # already liked, so unlike
                like.delete()
            return redirect("blog-detail", slug=self.object.slug)

        # Handle Comment
        elif "comment" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = self.object
                comment.save()
            return redirect("blog-detail", slug=self.object.slug)

        return redirect("blog-detail", slug=self.object.slug)


def get_client_ip(request):
    """Extract client IP for Like tracking"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
