from django.db import migrations, models
from django.contrib.auth.models import Group, Permission

def make_permissions(apps, schema_editor):
    employees = Group(name="employee", id=0)
    managers = Group(name="manager", id=1)
    
    employees.save()
    managers.save()

class Migration(migrations.Migration):

    dependencies = [('account', '0001_initial',), ('account', '0002_useraccount_cart'), ('account', '0003_useraccount_hourly_wage_useraccount_hours_worked')]

    operations = [
        migrations.RunPython(make_permissions),
    ]