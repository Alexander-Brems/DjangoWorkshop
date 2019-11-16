from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()

    def get_absolute_url(self):
        return reverse('note-list')