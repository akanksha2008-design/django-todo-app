from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)   # Required field
    description = models.TextField(blank=True) # Optional field
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
