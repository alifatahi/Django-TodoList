from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()[:10]
    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)


def details(request, id):
    todo = ToDo.objects.get(id=id)
    context = {
        'todo': todo
    }

    return render(request, 'details.html', context)
