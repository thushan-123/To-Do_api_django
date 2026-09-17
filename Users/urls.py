from django.urls import path
from . import views

urlpatterns = [
    #create
    path('register', views.registerUser, name='registerUser'),

    # all users
    path('loggin', views.getUser, name='getUser'),

    # update user
    path('update/<int:user_id>', views.updateUser, name='updateUser'),

    # delete
    path('delete/<int:user_id>', views.deleteUser, name='deleteUser'),
]

