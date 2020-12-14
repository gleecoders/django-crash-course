from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)


def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, "todo/todo_detail.html", context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # print(form.cleaned_data)
        # 
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, "todo/todo_create.html", context)

