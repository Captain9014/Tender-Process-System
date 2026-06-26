from django.urls import path
from . import views

urlpatterns = [

    path(
        'assigned-projects/',
        views.assigned_projects,
        name='assigned_projects'
    ),

]