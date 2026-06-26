from django.urls import path
from . import views

urlpatterns = [

    path(
        'chat-room/<int:id>/',
        views.chat_room,
        name='chat_room'
    ),

     path(
        'edit-message/<int:id>/',
        views.edit_message,
        name='edit_message'
    ),

    path(
        'delete-message/<int:id>/',
        views.delete_message,
        name='delete_message'
    ),
]