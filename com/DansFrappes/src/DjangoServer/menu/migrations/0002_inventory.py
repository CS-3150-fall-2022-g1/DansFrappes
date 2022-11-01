from django.db import migrations
from menu.models import Ingredient

def add_inventory(apps, schema_editor):

    ## Add-ins
    carmel = Ingredient(name="carmel", stock=1000, buy_cost=0.15, sell_cost=0.30)
    carmel.save()
    chocolate = Ingredient(name="chocolate", stock=1000, buy_cost=0.15, sell_cost=0.30)
    chocolate.save()
    espresso = Ingredient(name="espresso", stock=1000, buy_cost=0.15, sell_cost=0.30)
    espresso.save()
    vanilla = Ingredient(name="vanilla", stock=1000, buy_cost=0.15, sell_cost=0.30)
    vanilla.save()
    peppermint = Ingredient(name="peppermint", stock=1000, buy_cost=0.15, sell_cost=0.30)
    peppermint.save()
    matcha = Ingredient(name="matcha", stock=1000, buy_cost=0.15, sell_cost=0.30)
    matcha.save()
    whipped_cream = Ingredient(name="whipped_cream", stock=1000, buy_cost=0.20, sell_cost=0.35)
    whipped_cream.save()

    ## Milks (10 stock is 1 gallons)
    milk_whole = Ingredient(name="milk_whole", stock=100, buy_cost=0.20, sell_cost=3.50)
    milk_whole.save()
    milk_skim = Ingredient(name="milk_skim", stock=100, buy_cost=0.20, sell_cost=3.50)
    milk_skim.save()
    milk_almond = Ingredient(name="milk_almond", stock=100, buy_cost=0.25, sell_cost=3.80)
    milk_almond.save()
    milk_cashew = Ingredient(name="milk_cashew", stock=100, buy_cost=0.35, sell_cost=4.00)
    milk_cashew.save()
    milk_oat = Ingredient(name="milk_oat", stock=100, buy_cost=0.37, sell_cost=4.10)
    milk_oat.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0001_initial')]

    operations = [
        migrations.RunPython(add_inventory),
    ]