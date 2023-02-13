from webapp.models import List
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def view(request: WSGIRequest):
    lists = List.objects.all()
    context = {
        'lists': lists
    }
    return render(request, 'home.html', context=context)
