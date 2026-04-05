"""Views for handling task logic, user registration, and statistics."""
# pylint: disable=no-member

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import AnswerForm

def task_list(request):
    """Display a list of all available physics tasks."""
    tasks = Task.objects.all()
    return render(request, 'simulator/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    """Display a specific task and handle physics answer validation."""
    task = get_object_or_404(Task, id=task_id)
    message = None
    form = AnswerForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user_val = form.cleaned_data['user_answer']

            if abs(user_val - task.correct_answer) <= 0.1:
                message = "Верно! Вы молодец."
            else:
                message = f"Неверно. Правильный ответ: {task.correct_answer}"

    return render(request, 'simulator/task_detail.html', {
        'task': task,
        'form': form,
        'message': message
    })

def statistics(request):
    """Display general statistics about the available tasks."""
    total_tasks = Task.objects.count()
    return render(request, 'simulator/statistics.html', {'total_tasks': total_tasks})

def register(request):
    """Handle new user registration using Django's built-in form."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
