from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    creator = models.ForeignKey(User, related_name='created_events', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participating_events', blank=True)

    def __str__(self):
        return self.title
