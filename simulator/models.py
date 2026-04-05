"""Data model description module for the PhysLab database."""
from django.db import models

class Task(models.Model):
    """A model of a physical problem with a condition and a correct answer."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    correct_answer = models.FloatField()
