from django.db import models

# Create your models here.
from django.db import models
class Hero(models.Model):
    hero_id = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    @property
    def details(self):
        return self.choice_set.all()

class Details(models.Model):
    hero_id = models.CharField(max_length=60)
    villian = models.CharField(max_length=60)
    universe = models.CharField(max_length=60)
    def __str__(self):
        return self.hero_id