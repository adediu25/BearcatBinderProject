from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.TodoItemView.as_view(), name="list"),
    # lists
    path("list/add/", views.CreateList.as_view(), name="list-add"),
    path("list/<int:pk>/delete/", views.DeleteList.as_view(), name="list-delete"),
    #items
    path("list/<int:list_id>/item/add/", views.CreateItem.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", views.UpdateItem.as_view(), name="item-update"),
    path("list/<int:list_id>/item/<int:pk>/delete/", views.DeleteItem.as_view(), name="item-delete",),
]