from django.contrib.auth.models import Group
from .models import UserAccount

def createAccount(email, first, last, password):
    '''
    Create a new user account
    '''
    user = UserAccount.objects.create_user(email, email, password)
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