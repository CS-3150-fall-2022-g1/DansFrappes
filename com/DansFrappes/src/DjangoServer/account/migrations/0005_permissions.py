from django.db import migrations, models
from django.contrib.auth.models import Group, Permission

def make_permissions(apps, schema_editor):
    employees = Group.objects.get(id=0)
    managers = Group.objects.get(id=1)

    

    # employees.permissions.add(Permission.objects.get(codename='handle_orders'))
    # managers.permissions.add(Permission.objects.get(codename='edit_employees'))
    # managers.permissions.add(Permission.objects.get(codename='order_inventory'))
    # managers.permissions.add(Permission.objects.get(codename='edit_menu'))

class Migration(migrations.Migration):

    dependencies = [('account', '0001_initial',), ('account', '0002_useraccount_cart'), ('account', '0003_useraccount_hourly_wage_useraccount_hours_worked'), ('account', '0004_groups')]

    operations = [
        migrations.RunPython(make_permissions),
    ]