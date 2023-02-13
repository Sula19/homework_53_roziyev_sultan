from webapp.models import List
from django.contrib import admin


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date']
    list_filter = ['id', 'date', 'status']
    search_fields = ['status', 'date']
    fields = ['description', 'status', 'date']


admin.site.register(List, ListAdmin)
