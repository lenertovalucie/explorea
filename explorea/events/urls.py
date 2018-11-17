from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.event_listing, name='events'),
    path('events/detail/<int:pk>', views.event_detail, name='detail'),
    path('events/update/<int:pk>', views.update_event, name='update_event'),
    path('events/delete/<int:pk>', views.delete_event, name='delete_event'),
    path('events/new/', views.create_event, name='create_event'),
    path('events/<int:event_id>/newRun/', views.create_event_run, name='create_event_run'),
    path('events/updateRun/<int:event_run_id>', views.update_event_run, name='update_event_run'),
    path('events/deleteRun/<int:event_run_id>', views.delete_event_run, name='delete_event_run'),
]