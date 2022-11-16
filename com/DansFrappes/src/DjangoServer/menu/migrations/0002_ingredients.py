from django.db import migrations
from menu.models import Ingredient, MilkIngredient

def add_inventory(apps, schema_editor):

    ## Add-ins
    caramel = Ingredient(name="Caramel", stock=1000, buy_cost=0.15)
    caramel.save()
    chocolate = Ingredient(name="Chocolate", stock=1000, buy_cost=0.15)
    chocolate.save()
    espresso = Ingredient(name="Espresso", stock=1000, buy_cost=0.15)
    espresso.save()
    vanilla = Ingredient(name="Vanilla", stock=1000, buy_cost=0.15)
    vanilla.save()
    peppermint = Ingredient(name="Peppermint", stock=1000, buy_cost=0.15)
    peppermint.save()
    matcha = Ingredient(name="Matcha", stock=1000, buy_cost=0.15)
    matcha.save()
    whipped_cream = Ingredient(name="Whipped Cream", stock=1000, buy_cost=0.20)
    whipped_cream.save()

    ## Milks (10 stock is 1 gallons)
    milk_whole = MilkIngredient(name="Whole", stock=100, buy_cost=0.20)
    milk_whole.save()
    milk_skim = MilkIngredient(name="Skim", stock=100, buy_cost=0.20)
    milk_skim.save()
    milk_almond = MilkIngredient(name="Almond", stock=100, buy_cost=0.25)
    milk_almond.save()
    milk_cashew = MilkIngredient(name="Cashew", stock=100, buy_cost=0.35)
    milk_cashew.save()
    milk_oat = MilkIngredient(name="Oat", stock=100, buy_cost=0.37)
    milk_oat.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0001_initial')]

    operations = [
        migrations.RunPython(add_inventory),
    ]
