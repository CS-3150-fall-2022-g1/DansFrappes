from account.models import UserAccount
from .models import Ingredient, Order, DrinkPreset, MilkIngredient
from decimal import Decimal

milk_markup = Decimal(4)
other_markup = Decimal(1.6)

def place_order(user):
    total = 0

    # Check for out of stock ingredients and calculate price
    # key is the name of the ingredient, value is the amount of the item
    
    for item in user.cart.get('items'):
        for key, value in item.items():
            ingredient = None
            if key == 'milk':
                ingredient = MilkIngredient.objects.get(name=value)
                total += ingredient.buy_cost * milk_markup
            else:
                ingredient = Ingredient.objects.get(name=key)
                total += ingredient.buy_cost * other_markup * Decimal(value)
    
    if user.funds > total:
        order = Order(user=user, order=user.cart, total=total)
        
        user.cart = get_empty_order()
        user.funds -= total 
        
        storeaccount = UserAccount.objects.get(store=True)
        storeaccount.funds += total

        user.save()
        order.save()
        storeaccount.save()

def add_item_to_cart(user, item):
    '''
    Validate an item and add it to the cart
    Returns true if sucessful, false if there was a validation error
    '''
    if len(item) == 0:
        return False
    try:
        for ingredient, amount in item.items():
            if ingredient=="milk":
                MilkIngredient.objects.get(name=amount)
            elif ingredient=="name":
                pass
            else:
                Ingredient.objects.get(name=ingredient)
                if amount <= 0 or amount > 9:
                    return False
    except: 
        return False

    user.cart['items'].append(item)
    user.save()
    return True

def get_empty_order():
    return {'items':[]}

def get_menu():
    return DrinkPreset.objects.all()

def get_unfulfilled():
    return Order.objects.get(fulfilled=False).order_by('-time')

def make_summary(user):
    summary = {'items':[]}
    total = 0

    for order in user.cart['items']:
        sum = make_item_summary(order)
        total += sum[0]
        summary['items'].append(sum[1])

    summary['total'] = total
    return summary

def make_item_summary(order):
    total = 0
    summary = {
        'name': order.get('name'),
        'ingredients':[]
    }

    for key, value in order.items():
        item = {}
        ingredient = None
        cost = 0
        amount = 1
        name = ""
        if key=="milk":
            ingredient = MilkIngredient.objects.get(name=value)
            cost = ingredient.buy_cost * milk_markup
            name = ingredient.name + " Milk"
        elif (key=="name"):
            summary['name'] = value
            continue
        else:
            ingredient = Ingredient.objects.get(name=key)
            cost = ingredient.buy_cost * other_markup
            amount = value
            name = ingredient.name

        cost = round(cost, 2)
        item['cost'] = cost
        item['name'] = name
        item['amount'] = amount
        summary['ingredients'].append(item)
        total += cost

    summary['total'] = total
    return [total, summary,]