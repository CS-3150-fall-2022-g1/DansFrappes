from django.db import migrations
from menu.models import DrinkPreset

def add_drinks(apps, schema_editor):
    drink1= DrinkPreset(name='Drink', order={
        'chocolate_pumps':2
    })
    drink1.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0003_drinkpresets')]

    operations = [
        migrations.RunPython(add_drinks),
    ]