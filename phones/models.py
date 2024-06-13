from django.db import models
from slugger import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(max_length=200, populate_from='name', unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
