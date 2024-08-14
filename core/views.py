from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Task


@login_required
def index(request):
    if request.method == "POST":
        task = request.POST.get("task")
        new_task = Task(user=request.user, name=task)
        new_task.save()
    tasks = Task.objects.all().filter(user=request.user, status=False)
    completed_tasks = Task.objects.all().filter(user=request.user, status=True)
    context = {"tasks": tasks, "completed_tasks": completed_tasks}
    return render(request, "core/index.html", context)


def update(request, name):
    task = Task.objects.get(user=request.user, name=name)
    task.status = True
    task.save()
    return redirect("core:index")


def delete(request, name):
    task = Task.objects.get(user=request.user, name=name)
    task.delete()
    return redirect("core:index")
