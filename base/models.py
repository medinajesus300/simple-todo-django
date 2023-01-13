from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    """
    Task model

    Fields:
    user: ForeignKey to auth.User
    title: CharField
    description: TextField
    complete: BooleanField
    created: DateTimeField
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # Class to order the tasks by the created date
    class Meta:
        ordering = ['complete', '-created']
        
