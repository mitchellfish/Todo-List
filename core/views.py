from django.shortcuts import render, redirect
from .models import Todo

def task_list(request):
    tasks = Todo.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Todo.objects.create(title=title, content=description)
        return redirect('task_list')

    return render(request, 'todo_list.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


def toggle_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')