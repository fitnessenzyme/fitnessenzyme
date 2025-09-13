from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('new/', BlogCreateView.as_view(), name='blog-create'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('<slug:slug>/edit/', BlogUpdateView.as_view(), name='blog-update'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
]
