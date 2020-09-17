from django.db import models


# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField()

    def __str__ (self):
        return self.title


