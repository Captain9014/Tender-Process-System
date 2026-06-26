from django.urls import path
from . import views

urlpatterns = [

    path(
        'update-progress/<int:id>/',
        views.update_progress,
        name='update_progress'
    ),

    path(
        'project-progress/<int:id>/',
        views.project_progress,
        name='project_progress'
    ),

]