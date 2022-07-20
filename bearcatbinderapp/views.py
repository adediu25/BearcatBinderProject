from django.shortcuts import render
from django.views.generic import ListView
from .models import List, Item

class TodoListView(ListView):
    model = List
    template_name = "bearcatbinderapp/index.html"

class TodoItemView(ListView):
    model = Item
    template_name = "bearcatbinderapp/index.html"

    def get_queryset(self):
        return Item.objects.filter(parent_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["parent_list"] = List.objects.get(id=self.kwargs["list_id"])
        return context