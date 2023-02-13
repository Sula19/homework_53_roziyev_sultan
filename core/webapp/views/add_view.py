from django.shortcuts import render,redirect
from webapp.models import List
from django.core.handlers.wsgi import WSGIRequest


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_view.html')
    list_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date')
    }
    lists = List.objects.create(**list_data)
    return redirect(f'/detail_view/?pk={lists.pk}')
