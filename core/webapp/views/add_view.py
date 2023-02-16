from django.shortcuts import render, redirect, reverse
from webapp.models import List
from django.core.handlers.wsgi import WSGIRequest


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_view.html')
    list_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'detailed_description': request.POST.get('detailed_description'),
        'status': request.POST.get('status'),
        'date': request.POST.get('date')
    }
    lists = List.objects.create(**list_data)
    reverse_url = reverse('detail_view', kwargs={'pk': lists.pk})
    return redirect(reverse_url)
