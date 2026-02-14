from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


# Display all tasks
def task_list(request):
    tasks = Task.objects.all().order_by('created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})


# Create new task
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title:
            Task.objects.create(title=title, description=description)
            return redirect('todo:task_list')

        error = "Title cannot be empty."
        return render(request, 'todo/task_form.html', {'error': error})

    return render(request, 'todo/task_form.html')


# Update task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'

        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return redirect('todo:task_list')

        return render(request, 'todo/task_form.html', {
            'task': task,
            'error': 'Title cannot be empty.'
        })

    return render(request, 'todo/task_form.html', {'task': task})


# Delete task
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('todo:task_list')

    return render(request, 'todo/task_confirm_delete.html', {'task': task})


# Toggle complete/incomplete
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('todo:task_list')
