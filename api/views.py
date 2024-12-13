from rest_framework import generics, permissions
from core.models import Task
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsUserReadOnly
from django.contrib.auth.models import User


class TaskListView(generics.ListCreateAPIView):
    permission_classes = [IsUserReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user, status="False")
    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= [IsUserReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
class DoneTaskLlistView(generics.ListAPIView):
    permission_classes = [IsUserReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user, status = "True")
    
class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset= User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AllTaskListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    

