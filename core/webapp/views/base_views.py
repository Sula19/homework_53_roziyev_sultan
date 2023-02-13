from webapp.models import List
from django.views.generic.edit import DeleteView, UpdateView


class ListUpdateView(UpdateView):
    model = List
    fields = [
        'description',
        'status',
        'date'
    ]
    template_name = 'update.html'
    success_url = '/'


class ListDeleteView(DeleteView):
    model = List
    template_name = 'delete.html'
    success_url = '/'