from django.db import models


# Create your models here.

POST_TYPE = (

('NOTE','NOTE'),

('BIG NOTE','BIG NOTE'),


)


class post(models.Model):
    title = models.CharField(max_length=50 , unique=True)
    content = models.TextField(max_length=2000 , null=True , blank= True)
    created_at = models.DateTimeField()
    active = models.BooleanField(default=False)
    author_mail = models.EmailField(default='')
    type = models.CharField(choices=POST_TYPE ,default='NOTE', max_length= 20)
    image = models.ImageField(upload_to='post/')
    def __str__ (self):
        return self.title


