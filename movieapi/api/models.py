# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    runningtime = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class Order(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    card = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name