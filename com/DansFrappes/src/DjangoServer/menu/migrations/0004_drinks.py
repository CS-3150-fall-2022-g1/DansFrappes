from django.db import migrations
from menu.models import DrinkPreset

def add_drinks(apps, schema_editor):
    drink1= DrinkPreset(name='The Josh', order={
        'name':'The Josh',
        'description':'TODO',
        'Chocolate':1,
        'Whipped Cream':3,
        'Matcha':1,
        'milk':"Whole"
    })
    drink1.save()
    drink2= DrinkPreset(name='The Jason', order={
        'name':'The Jason',
        'description':'TODO',
        'Chocolate':2,
        'milk':"Whole"
    })
    drink2.save()
    drink3= DrinkPreset(name='The Spencer', order={
        'name':'The Spencer',
        'description':'TODO',
        'Chocolate':2,
        'milk':"Whole"
    })
    drink3.save()
    
    drink4= DrinkPreset(name='The Reagan', order={
        'name':'The Reagan',
        'description':'TODO',
        'Chocolate':2,
        'milk':"Whole"
    })
    drink4.save()
    drink5= DrinkPreset(name='The Dan', order={
        'name':'The Dan',
        'description':'TODO',
        'Chocolate':2,
        'milk':"Whole"
    })
    drink5.save()
    drink6= DrinkPreset(name='The Andrew', order={
        'name':'The Andrew',
        'description':'TODO',
        'Chocolate':2,
        'milk':"Whole"
    })
    drink6.save()

class Migration(migrations.Migration):

    dependencies = [('menu', '0003_drinkpreset_description_drinkpreset_image_and_more')]

    operations = [
        migrations.RunPython(add_drinks),
    ]