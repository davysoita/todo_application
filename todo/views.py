from django.shortcuts import render, redirect

from .form import TaskForm
from .models import Task
# Create your views here.
def task_list(request):
    # all records n the database are captured
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks':tasks})
def create_task(request):
    # check validity of the form
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'todo/task_form', {'form':form})
