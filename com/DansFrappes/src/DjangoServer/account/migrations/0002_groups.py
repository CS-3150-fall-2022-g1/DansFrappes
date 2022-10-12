from django.db import migrations, models
from django.contrib.auth.models import Group, Permission

def make_permissions(apps, schema_editor):
    employees = Group(name="employee", id=0)
    managers = Group(name="manager", id=1)
    
    employees.save()
    managers.save()

    employees.permissions.add(Permission.objects.get(codename='handle_orders'))

    managers.permissions.add(Permission.objects.get(codename='edit_employees'))
    managers.permissions.add(Permission.objects.get(codename='order_inventory'))
    managers.permissions.add(Permission.objects.get(codename='edit_menu'))


class Migration(migrations.Migration):

    dependencies = [('account', '0001_initial')]

    operations = [
        migrations.RunPython(make_permissions),
    ]