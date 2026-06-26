from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('client-dashboard/', views.client_dashboard),
    path('builder-dashboard/', views.builder_dashboard),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('block-builder/<int:id>/', views.block_builder, name='block_builder'),
    path('block-user/<int:id>/', views.block_user, name='block_user'),
    path('unblock-user/<int:id>/', views.unblock_user, name='unblock_user'),

]
