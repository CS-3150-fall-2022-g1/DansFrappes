from django.db import migrations
from menu.models import DrinkPreset

def add_drinks(apps, schema_editor):
    drink1= DrinkPreset(name='The Josh', order={
        'chocolates_pump':1,
        'whipped_cream':3,
        'matcha':1,
        'milk':"Whole"
    })
    drink1.save()
    drink2= DrinkPreset(name='The Jason', order={
        'chocolate_pumps':2,
        'milk':"Whole"
    })
    drink2.save()
    drink3= DrinkPreset(name='The Spencer', order={
        'chocolate_pumps':2,
        'milk_whole':1
    })
    drink3.save()
    drink4= DrinkPreset(name='The Reagan', order={
        'chocolate_pumps':2,
        'milk_whole':1
    })
    drink4.save()
    drink5= DrinkPreset(name='The Dan', order={
        'chocolate_pumps':2
    })
    drink5.save()
    drink6= DrinkPreset(name='The Andrew', order={
        'chocolate_pumps':2,
        'milk_whole':1
    })
    drink6.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0002_ingredients')]

    operations = [
        migrations.RunPython(add_drinks),
    ]