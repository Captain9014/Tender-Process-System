from django.urls import path
from . import views

urlpatterns = [

    path(
        'create-tender/',
        views.create_tender,
        name='create_tender'
    ),

]