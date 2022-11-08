from .models import Ingredient, Order, DrinkPreset, MilkIngredient

milk_markup = 4
other_markup = 1.6

def place_order(user):
    total = 0

    # Check for out of stock ingredients and calculate price
    # key is the name of the ingredient, value is the amount of the item
    
    for item in user.cart.get('items'):
        for key, value in item.items():
            if key == 'milk':
                ingredient = MilkIngredient.objects.get(name=value)
                total += ingredient.buy_cost * milk_markup * value
            ingredient = Ingredient.objects.get(name=key)
            total += ingredient.buy_cost * other_markup * value

    order = Order(user=user, order=user.cart, total=total)
    order.save()
    user.cart = get_empty_order()
    user.save()

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