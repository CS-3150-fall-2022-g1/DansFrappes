from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.
class Order(models.Model):

    user = models.ForeignKey('account.UserAccount', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.DateTimeField(auto_now=True)
    order = models.JSONField()
    fulfilled = models.BooleanField(default=False)
    
class Ingredient(models.Model):
    ''' Model for the inventory table. '''
    # image = 
    name = models.CharField(max_length=15)
    stock = models.IntegerField()

    # These costs cannot be above $99.99 per ingredient
    buy_cost = models.DecimalField(max_digits=4, decimal_places=2)
    sell_cost = models.DecimalField(max_digits=4, decimal_places=2)

class DrinkPreset(models.Model):
    name = models.CharField(max_length=20)
    order = models.JSONField()

class MilkIngredient(Ingredient):
    pass