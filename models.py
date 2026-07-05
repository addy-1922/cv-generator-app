from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    #address = models.TextField()
    summary = models.TextField(max_length=2000)
    previous_work= models.TextField(max_length=1000)
    skills = models.TextField(max_length=100)

    ''' def __str__(self):
        return self.name'''
