from django.urls import path
from . import views

urlpatterns = [
    #create
    path('user/register/', views.registerUser, name='registerUser'),

    # all users
    path('users/', views.getUsers, name='getUsers'),

    # update user
    path('user/update/', views.updateUser, name='updateUser'),

    # delete
    path('user/delete/', views.deleteUser, name='deleteUser'),
]

