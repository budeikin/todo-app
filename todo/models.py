from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = "user"


# class TaskLine(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True,null=True)
#     task = models.ForeignKey('Task',on_delete=models.CASCADE,related_name='tasklines')
#     is_completed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.task.title
