from django.db import migrations
from menu.models import DrinkPreset

def add_drinks(apps, schema_editor):
    drink1= DrinkPreset(name='The Josh', order={
        'chocolate_pumps':2
    })
    drink1.save()
    drink2= DrinkPreset(name='The Jason', order={
        'chocolate_pumps':2
    })
    drink2.save()
    drink3= DrinkPreset(name='The Spencer', order={
        'chocolate_pumps':2
    })
    drink3.save()
    drink4= DrinkPreset(name='The Reagan', order={
        'chocolate_pumps':2
    })
    drink4.save()
    drink5= DrinkPreset(name='The Dan', order={
        'chocolate_pumps':2
    })
    drink5.save()
    drink6= DrinkPreset(name='The Andrew', order={
        'chocolate_pumps':2
    })
    drink6.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0003_drinkpresets')]

    operations = [
        migrations.RunPython(add_drinks),
    ]