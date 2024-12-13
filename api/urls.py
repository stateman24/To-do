from django.urls import path
from .views import TaskListView, UserListView, DoneTaskLlistView, UserDetailView, TaskDetailView, AllTaskListView

app_name = "api"

urlpatterns = [
    path("v1/tasklist/", TaskListView.as_view(), name="task_list"),
    path("v1/task/<int:pk>/", TaskDetailView.as_view(), name="task"),
    path("v1/admin/users/", UserListView.as_view(), name="admin_users"),
    path("v1/admin/tasks/", AllTaskListView.as_view(), name="admin_all_tasks"),
    path("v1/admin/users/<int:pk>/", UserDetailView.as_view(), name="admin_users_details"),
    path("v1/tasklist/done", DoneTaskLlistView.as_view(), name="tasks_done"),
]
