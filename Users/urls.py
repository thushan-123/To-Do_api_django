from django.urls import path
from . import views

urlpatterns = [
    #create
    path('register', views.registerUser, name='registerUser'),

    # all users
    path('users', views.getUsers, name='getUsers'),

    # update user
    path('update', views.updateUser, name='updateUser'),

    # delete
    path('delete', views.deleteUser, name='deleteUser'),
]

