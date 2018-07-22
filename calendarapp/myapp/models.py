from django.db import models

# model Entry
class Entry(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

#returns name of Entry

    def __str__(self):
        return f'{self.name} {self.date}'
