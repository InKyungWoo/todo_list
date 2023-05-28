from django.db import models

# todo->models.py
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    complete = models.BooleanField(default=False) 

    def __str__(self):
        return self.description