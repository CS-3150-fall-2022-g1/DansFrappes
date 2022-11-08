from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from menu.utils import get_empty_order

# Create your models here.
class UserAccount(AbstractUser):
    #Add custom fields here
    
    birthday = models.DateField(default=None, blank=True, null=True)
    funds = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    cart = models.JSONField(default=get_empty_order)
    hourly_wage = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    hours_worked = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    employee = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    store = models.BooleanField(default=False)


    def setCustomer(self):
        """
        Remove this user from groups. This is only needed when removing permissions from an employee.
        """
        self.groups.clear()
        self.manager = False
        self.employee = False
        self.save()
        return self

    def setEmployee(self):
        """
        Move this user to the 'employee' group
        """
        self.groups.clear()
        group = Group.objects.get(name="employee")
        self.groups.add(group)
        self.hourly_wage = 15.00
        self.employee = True
        self.manager = False
        self.save()
        return self

    def isEmployee(self):
        return self.employee
    
    def isManager(self):
        return self.manager

    def setManager(self):
        """
        Move this user to the 'manager' group
        """
        self.groups.clear
        employeeGroup = Group.objects.get(name="employee")
        managerGroup = Group.objects.get(name="manager")
        self.groups.add(employeeGroup)
        self.groups.add(managerGroup)
        self.hourly_wage = 400.00
        self.manager = True
        self.employee = True
        self.save()
        return self

    def pay(self):
        self.funds += self.hourly_wage * self.hours_worked
        self.hours_worked = 0.0
        self.save()
        return self

    def setWage(self, wage):
        self.hourly_wage = wage
        self.save()
        return self

    class Meta:
        permissions = [
            ("edit_employees", "Can add, remove, and pay employees"),
            ("handle_orders", "Can view employee pages"),
            ("order_inventory", "Can order additional inventory"),
            ("edit_menu", "Can add or remove menu items")
        ]