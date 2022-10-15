from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
class UserAccount(AbstractUser):
    #Add custom fields here


    def setUserCustomer(self, request):
        """
        Remove this user from groups
        """
        self.groups.clear()
        return self

    def setEmployee(self, request):
        """
        Move this user to the 'employee' group
        """
        self.groups.clear()
        group = Group.objects.get(name="employee")
        self.user.groups.add(group)
        return self

    def setManager(self, request):
        """
        Move this user to the 'manager' group
        """
        self.groups.clear
        employeeGroup = Group.objects.get(name="employee")
        managerGroup = Group.objects.get(name="manager")
        self.groups.add(employeeGroup)
        self.groups.add(managerGroup)
        return self

    class Meta:
        permissions = [
            ("edit_employees", "Can add, remove, and pay employees"),
            ("handle_orders", "Can view employee pages"),
            ("order_inventory", "Can order additional inventory"),
            ("edit_menu", "Can add or remove menu items")
        ]