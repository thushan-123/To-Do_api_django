import uuid

from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    # user_id =
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title