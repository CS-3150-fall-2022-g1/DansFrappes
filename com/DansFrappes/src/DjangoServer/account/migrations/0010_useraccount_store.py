# Generated by Django 3.2.8 on 2022-11-06 23:29

from django.db import migrations, models

from account.models import UserAccount


class Migration(migrations.Migration):
    def add_admin(apps, schema_editor):
        admin = UserAccount.objects.create_user("admin", "admin@gmail.com", "password")
        admin.first_name = "admin"
        admin.last_name = " "
        admin.setManager()
        admin.store = True
        admin.save()

    dependencies = [
        ('account', '0009_alter_useraccount_funds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='store',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(add_admin),
    ]