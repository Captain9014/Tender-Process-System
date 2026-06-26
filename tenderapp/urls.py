from django.urls import path
from . import views

urlpatterns = [

    path(
        'create-tender/',
        views.create_tender,
        name='create_tender'
    ),

    path(
        'my-tenders/',
        views.my_tenders,
        name='my_tenders'
    ),

    path(
    'edit-tender/<int:id>/',
    views.edit_tender,
    name='edit_tender'
    ),

    path(
    'delete-tender/<int:id>/',
    views.delete_tender,
    name='delete_tender'
    ),

    path(
    'available-tenders/',
    views.available_tenders,
    name='available_tenders'
    ),

    path(
    'view-bids/<int:id>/',
    views.view_bids,
    name='view_bids'
    ),

    path(
    'select-builder/<int:id>/',
    views.select_builder,
    name='select_builder'
    ),
    
    path(
    'complete-project/<int:id>/',
    views.complete_project,
    name='complete_project'
),

]