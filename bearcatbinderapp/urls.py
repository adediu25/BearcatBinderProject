from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.TodoItemView.as_view(), name="list")
]