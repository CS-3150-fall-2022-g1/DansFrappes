# Generated by Django 4.0.2 on 2022-11-02 18:02

from django.db import migrations, models
from account.models import UserAccount

class Migration(migrations.Migration):
    

    dependencies = [
        ('account', '0006_alter_useraccount_hours_worked'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='manager',
            field=models.BooleanField(default=False),
        ),
       
    ]