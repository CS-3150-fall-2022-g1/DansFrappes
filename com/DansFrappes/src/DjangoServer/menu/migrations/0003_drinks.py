from django.db import migrations
from menu.models import DrinkPreset

def add_drinks(apps, schema_editor):
    drink1= DrinkPreset(name='The Josh', order={
        'Chocolate':1,
        'Whipped Cream':3,
        'Matcha':1,
        'milk':"Whole"
    })
    drink1.save()
    drink2= DrinkPreset(name='The Jason', order={
        'Chocolate':2,
        'milk':"Whole"
    })
    drink2.save()
    drink3= DrinkPreset(name='The Spencer', order={
        'Chocolate':2,
        'milk':"Whole"
    })
    drink3.save()
    drink4= DrinkPreset(name='The Reagan', order={
        'Chocolate':2,
        'milk':"Whole"
    })
    drink4.save()
    drink5= DrinkPreset(name='The Dan', order={
        'Chocolate':2,
        'milk':"Whole"
    })
    drink5.save()
    drink6= DrinkPreset(name='The Andrew', order={
        'Chocolate':2,
        'milk':"Whole"
    })
    drink6.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0002_ingredients')]

    operations = [
        migrations.RunPython(add_drinks),
    ]