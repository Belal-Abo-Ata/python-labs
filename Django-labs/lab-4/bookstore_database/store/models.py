from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    rate = models.IntegerField()
    views = models.IntegerField()

    def __str__(self):
        return self.title
