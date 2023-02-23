from django.shortcuts import render, redirect
from webapp.forms import ListForms
from webapp.models import List
from django.core.handlers.wsgi import WSGIRequest


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = ListForms()
        return render(request, 'add_view.html', context={
            'form': form
        })

    form = ListForms(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_view.html', context={
            'form': form
        })
    else:
        List.objects.create(**form.cleaned_data)
        return redirect('view')
