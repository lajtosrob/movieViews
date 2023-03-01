from django.db import models

class Item(models.Model):
    text=models.CharField(max_length=255)
    done=models.BooleanField(default=False)

# Create your models here.
