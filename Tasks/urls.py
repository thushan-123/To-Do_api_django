from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:user_id>', views.filter_tasks, name='filter_tasks'),
    path('create', views.create_task, name='create_task'),
    path('update/<int:task_id>', views.update_task, name='update_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
]