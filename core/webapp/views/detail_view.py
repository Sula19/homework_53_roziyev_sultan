from django.shortcuts import render
from webapp.models import List
from django.core.handlers.wsgi import WSGIRequest


def detail_view(request: WSGIRequest):
    list_id = request.GET.get('pk')
    lists = List.objects.get(pk=list_id)
    context = {
        'list': lists
    }
    return render(request, 'detail_view.html', context=context)
