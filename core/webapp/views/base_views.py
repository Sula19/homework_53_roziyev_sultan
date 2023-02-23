from webapp.forms import ListForms
from webapp.models import List
from django.shortcuts import redirect, render, get_object_or_404



def delete(request, pk):
    if request.method == 'GET':
        lists = List.objects.get(pk=pk)
        return render(request, 'delete.html', context={'lists': lists})
    if request.method == 'POST':
        lists = List.objects.get(pk=pk)
        lists.delete()
    return redirect('view')


def update(request, pk):
    lists = get_object_or_404(List, pk=pk)
    if request.method == 'POST':
        form = ListForms(request.POST, instance=lists)
        if form.is_valid():
            form.save()
            return redirect('view')
        return render(request, 'update.html', context={'form': form})
    form = ListForms(instance=lists)
    return render(request, 'update.html', context={'form': form})
