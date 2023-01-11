from django.db import models

# Create your models here.
class Candle(models.Model):
    no = models.indexes
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # default string(for list)
    def __str__(self):
        return f'[{self.pk}]{self.title}'