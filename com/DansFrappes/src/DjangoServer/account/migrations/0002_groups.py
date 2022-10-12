from django.db import migrations, models
from django.contrib.auth.models import Group, Permission

def make_permissions(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.

    edit_employees = Permission(codename="edit_employees")
    edit_employees.save()

    order_inventory = Permission(codename="order_inventory")
    order_inventory.save()
    
    handle_order = Permission(codename="handle_order")
    handle_order.save()

    employees = Group(name="employee")
    employees.permissions.set(['account.handle_order'])
    employees.save()

    managers = Group(name="manager")
    managers.permissions.set(['account.edit_employees', 'account.order_inventory'])
    managers.save()

class Migration(migrations.Migration):

    dependencies = [('account', '0001_initial')]

    operations = [
        migrations.RunPython(make_permissions),
    ]