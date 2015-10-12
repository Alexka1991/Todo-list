from django.http import HttpResponse
from django.shortcuts import render, redirect

from models import Todo
from todo.list.forms import TodoForm


def todo_form(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('todo')
    return render(request, 'form.html', locals())


def todo(request):
    form = TodoForm(request.POST)
    todos = Todo.objects.all().order_by('-created')
    return render(request, 'todo.html', locals())


def del_todo(request, id):
    del_todo = Todo.objects.get(id=id)
    del_todo.delete()
    return HttpResponse('OK')