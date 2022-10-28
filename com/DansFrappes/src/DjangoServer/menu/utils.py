from .models import Ingredient, Order

def place_order(user):
    total = 0

    # Check for out of stock ingredients and calculate price
    # key is the name of the ingredient, value is the amount of the item 
    
    for item in user.cart.get('items'):
        for key, value in item.items():
            ingredient = Ingredient.objects.get(name=key)
            total += ingredient.sell_cost * value

    order = Order(user=user, order=user.cart, total=total)
    order.save()
    user.cart = get_empty_order()
    user.save()

def add_item_to_cart(user, item):
    user.cart['items'].append(item)
    user.save()

def add_topping():
    #TODO - we need a function to add toppings
    pass

def get_empty_order():
    return {'items':[]}