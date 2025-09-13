from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.home, name="home"), 

    # Accounts URLs
    path('accounts/', include('accounts.urls')),

    # Blog URLs
    path('blogs/', include('blogs.urls')),

    # Redirect root '/' to blog list
    path('', lambda request: redirect('blog-list')),

    # CKEditor URLs
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
