from django.contrib.auth.models import Group

def pay_employees():
    employees = Group.objects.get(name="employee")
    store = Group.objects.get(name="manager")[0]
    for user in employees.user_set.all():
        pay = user.hourly_wage * user.hours_worked
        store.funds -= pay
        user.funds += pay