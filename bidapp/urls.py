from django.urls import path
from . import views

urlpatterns=[

path(
'submit-bid/<int:id>/',
views.submit_bid,
name='submit_bid'
)

]