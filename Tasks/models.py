
from django.db import models

from Users.models import User


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title