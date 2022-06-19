from django.db import models


# Create your models here.
class Func(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
