"""Administrative panel configuration module for the simulator application."""
from django.contrib import admin
from .models import Task

admin.site.register(Task)
