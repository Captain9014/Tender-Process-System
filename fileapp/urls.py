from django.urls import path
from . import views

urlpatterns = [

    path(
        'upload-file/<int:id>/',
        views.upload_file,
        name='upload_file'
    ),

    path(
        'project-files/<int:id>/',
        views.project_files,
        name='project_files'
    ),

]