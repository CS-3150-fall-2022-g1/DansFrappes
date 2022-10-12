from django.contrib.auth.models import Group
from django.contrib.auth.models import User

def createAccount(request, email, first, last, password):
    '''
    Create a new user account
    request: request of account making user (check permissions)
    '''
    user = User.objects.create_user(email, email, password)
    user.first_name = first
    user.last_name = last
    user.save()
    return user

def updateAccountData(user, email, first, last, password):
    """
    Update the user with info from the accountInfo dictionary
    """
    user.email = email
    user.first_name = first
    user.last_name = last
    user.password = password
    user.save()

def setUserCustomer(user):
    """
    Move a user to the 'customer' group
    """
    group = Group.objects.get(name="employee")
    user.groups.add(group)
    return user

def setUserEmployee(user):
    """
    Move a user to the 'employee' group
    """
    user.groups.clear()
    group = Group.objects.get(name="employee")
    user.groups.add(group)
    return user

def setUserManager(user):
    """
    Move a user to the 'manager' group
    """
    employeeGroup = Group.objects.get(name="employee")
    managerGroup = Group.objects.get(name="manager")
    user.groups.add(employeeGroup)
    user.groups.add(managerGroup)
    return user