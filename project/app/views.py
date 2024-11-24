from django.shortcuts import render,redirect, get_object_or_404
from app.models import Task
from app.form import TaskInfo

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

# Добавление задачи
def add_task(request):
    if request.method == 'POST':
        form = TaskInfo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = TaskInfo()
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')  


# Create your views here.
