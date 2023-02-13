from webapp.views.view import view
from webapp.views.base_views import ListDeleteView, ListUpdateView
from webapp.views.add_view import add_view
from webapp.views.detail_view import detail_view
from django.urls import path


urlpatterns = [
    path('', view),
    path('add_view/', add_view),
    path('detail_view/', detail_view),
    path('<pk>/delete/', ListDeleteView.as_view(), name='delete'),
    path('<pk>/update/', ListUpdateView.as_view(), name='update')
]