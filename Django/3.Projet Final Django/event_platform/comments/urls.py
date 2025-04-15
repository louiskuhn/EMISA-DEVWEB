from django.urls import path
from . import views

urlpatterns = [
    path('event/<int:event_id>/add/', views.add_comment, name='add_comment'),
    path('delete/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
]

