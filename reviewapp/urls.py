from django.urls import path
from . import views

urlpatterns = [

    path(
        'give-review/<int:id>/',
        views.give_review,
        name='give_review'
    ),

]