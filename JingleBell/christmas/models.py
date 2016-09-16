from django.db import models

# Create your models here.
class Decoration(models.Model):
    location = models.CharField(max_length=20)
    christmas_trees = models.IntegerField(default=0)
    gifts = models.IntegerField(default=0)