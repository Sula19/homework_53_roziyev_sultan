from webapp.views.base_views import delete, update
from webapp.views.view import view
from webapp.views.add_view import add_view
from webapp.views.detail_view import detail_view
from django.urls import path


urlpatterns = [
    path('', view, name='view'),
    path('add_view/', add_view, name='add_view'),
    path('detail_view/<int:pk>', detail_view, name='detail_view'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update')
]