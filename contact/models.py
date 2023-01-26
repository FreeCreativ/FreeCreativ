from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
