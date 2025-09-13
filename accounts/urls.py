from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name="delete-comment"),
]






