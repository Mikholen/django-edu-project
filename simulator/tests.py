"""Unit tests for the simulator application."""
from django.test import TestCase
from django.urls import reverse

class SimpleTest(TestCase):
    """Basic diagnostic tests for the simulator."""

    def test_task_list_status_code(self):
        """Check if the task list page loads correctly."""
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
