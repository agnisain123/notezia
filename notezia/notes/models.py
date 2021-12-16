from django.db import models

# Create your models here.
class Note(models.Model):
    route = models.CharField(max_length = 180)
    password = models.CharField(max_length= 256)
    content = models.TextField()

    def __str__(self):
        return self.route
