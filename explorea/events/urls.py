from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.event_listing, name='events'),
    path('events/new', views.event_new, name='new'),
    path('event/<str:name>', views.event_detail, name='detail'),
    path('event/<str:name>/edit', views.event_edit, name='edit'),
    path('event/<str:name>/delete', views.event_delete, name='delete'),
]