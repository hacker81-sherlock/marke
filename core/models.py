from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username

class Products(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='No Description')
    price = models.IntegerField()
    image = models.URLField(default='https://via.placeholder.com/150')

    def __str__(self):
        return self.title
