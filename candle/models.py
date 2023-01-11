from django.db import models

# Create your models here.
class Candle(models.Model):
    no = models.indexes
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
