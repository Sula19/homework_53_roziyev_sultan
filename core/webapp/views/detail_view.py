from django.shortcuts import render
from webapp.models import List
from django.core.handlers.wsgi import WSGIRequest


def detail_view(request: WSGIRequest, pk):
    lists = List.objects.get(pk=pk)
    context = {
        'list': lists
    }
    return render(request, 'detail_view.html', context=context)
