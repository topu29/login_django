from django.db import models

# Create your models here.

class Userlogin(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    def __str__(self):
        return self.username
