from unicodedata import decimal, name
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    hour_value = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.URLField(max_length=255, null=False, blank=False)


class Match(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE, related_name='matches',null=False, blank=False)

