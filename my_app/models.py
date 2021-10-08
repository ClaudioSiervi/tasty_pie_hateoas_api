from django.db import models

# Create your models here.

class MyModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
