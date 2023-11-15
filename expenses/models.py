from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Expenses(models.Model):

    """In this class we try to write our expenses"""

    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
