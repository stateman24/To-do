from django.urls import path
from core.views import index, update, delete

app_name = "core"

urlpatterns = [
    path('', index, name="index"),
    path("update/<str:name>/", update, name="update"),
    path('delete/<str:name>/', delete, name="delete")
]
