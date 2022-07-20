from django.db import models

# Create your models here.

from django.utils import timezone
from django.urls import reverse

class List(models.Model):
    title = models.CharField(max_length=100, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self):
        return self.title

class Item(models.Model):
    # doesn't need to be unique, could have recurring event
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=(timezone.now() + timezone.timedelta(days=1)))
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.parent_list.id), str(self.id)])

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]