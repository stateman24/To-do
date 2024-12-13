from django.urls import path
from .views import TaskListView

app_name = "api"

urlpatterns = [
    path("v1/tasklist/", TaskListView.as_view(), name="task_list")
]
