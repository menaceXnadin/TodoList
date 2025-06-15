from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from django import forms
from django.contrib.auth import logout



# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        due_date = request.POST.get('due_date') or None

        Task.objects.create(
            title=title,
            description=description,
            completed=completed,
            due_date=due_date,
            user=request.user  # Associate task with the logged-in user
        )

        return redirect('index')  # Redirect to avoid form resubmission

    tasks = Task.objects.filter(user=request.user)  # Uses ordering from Task.Meta
    return render(request, 'todo/index.html', {'tasks': tasks})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title', task.title)
        task.description = request.POST.get('description', task.description)
        task.due_date = request.POST.get('due_date') or None
        task.completed = 'completed' in request.POST  # ✅ capture checkbox

        if not task.title:
            messages.error(request, 'Title is required.')
            return redirect('edit_task', task_id=task.id)

        task.save()
        messages.success(request, 'Task updated successfully.')
        return redirect('index')

    return render(request, 'todo/edit_task.html', {'task': task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('index')

    return render(request, 'todo/delete_task.html', {'task': task})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    messages.success(request, 'Task marked as completed.')
    return redirect('index')

