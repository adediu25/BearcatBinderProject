from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import List, Item

class TodoListView(ListView):
    model = List
    template_name = "bearcatbinderapp/index.html"

class TodoItemView(ListView):
    model = Item
    template_name = "bearcatbinderapp/list.html"

    def get_queryset(self):
        return Item.objects.filter(parent_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["parent_list"] = List.objects.get(id=self.kwargs["list_id"])
        return context
class CreateList(CreateView):
    model = List
    fields = ["title"]

    def get_context_data(self):
        context = super(CreateList, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class CreateItem(CreateView):
    model = Item
    fields = [
        "parent_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(CreateItem, self).get_initial()
        parent_list = List.objects.get(id=self.kwargs["list_id"])
        initial_data["parent_list"] = parent_list
        return initial_data

    def get_context_data(self):
        context = super(CreateItem, self).get_context_data()
        parent_list = List.objects.get(id=self.kwargs["list_id"])
        context["parent_list"] = parent_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.parent_list_id])

class UpdateItem(UpdateView):
    model = Item
    fields = [
        "parent_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(UpdateItem, self).get_context_data()
        context["parent_list"] = self.object.parent_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.parent_list_id])

class DeleteList(DeleteView):
    model = List
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class DeleteItem(DeleteView):
    model = Item

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parent_list"] = self.object.parent_list
        return context

