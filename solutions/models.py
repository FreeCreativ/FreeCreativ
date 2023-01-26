from django.db import models

from django.utils import timezone


class Clients(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300, default='address')


class Solution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    year_of_project = models.DateField('year of project', default=timezone.now())
