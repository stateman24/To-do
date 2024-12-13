from rest_framework import generics, permissions
from core.models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserListView(generics.ListAPIView):
    queryset= User.objects.all()
    permission_classes = (permissions.IsAdminUser)
    serializer_class = UserSerializer
    

