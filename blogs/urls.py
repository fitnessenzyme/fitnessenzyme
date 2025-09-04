from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blogs, name='blog_list'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
