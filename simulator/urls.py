"""URL configuration for the simulator application."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('stats/', views.statistics, name='statistics'),
    path('register/', views.register, name='register'),
]
