'''employee model code is here'''
from django.db import models

class User(models.Model):
    '''user models'''
    name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.name
