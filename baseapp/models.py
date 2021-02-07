from django.db import models

# Create your models here.

class Mess(models.Model):
    roll_starts_with = models.PositiveIntegerField()
    hostel_name = models.CharField(max_length=50)
    menu_img = models.ImageField()

    def __str__(self):
        return self.hostel_name


class Event(models.Model):
    title = models.CharField(max_length=200)
    event_img = models.ImageField()
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title
    