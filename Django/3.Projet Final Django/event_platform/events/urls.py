from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('event/create/', views.EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', views.EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', views.EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/register/', views.register_event, name='register_event'),
    path('event/<int:pk>/unregister/', views.unregister_event, name='unregister_event'),
]

