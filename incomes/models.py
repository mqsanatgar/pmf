from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Incomes(models.Model):

    """Docstring for Incomes."""

    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
