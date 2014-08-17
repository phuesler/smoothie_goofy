from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Recipe(models.Model):
    name        = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

