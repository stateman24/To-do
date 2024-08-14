from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=225)
    status = models.BooleanField(default=False,)

    def __str__(self):
        return self.name
