from django.test import TestCase
from account.models import UserAccount
from .models import Ingredient, MilkIngredient
from .utils import add_item_to_cart, place_order, get_unfulfilled, make_summary, milk_markup, other_markup

# Create your tests here.
class Tests(TestCase):

    def setUp(self):
        UserAccount.objects.create_user('test', 'test@dansfrappes.com', 'password')

    def test_add_cart(self):
        print("Add to cart tests...")
        orderItem1 = {
            "name": "testdrink",
            "milk": "Oat",
            "Chocolate": 5
        }
        user = UserAccount.objects.get(email='test@dansfrappes.com')
        add_item_to_cart(user, orderItem1)
        self.assertEqual(user.cart.get('items')[0].get('name'), 'testdrink')

        orderItem2 = {
            "name": "testdrink2",
            "Matcha": 9,
            "Chocolate": 2
        }
        
        add_item_to_cart(user, orderItem2)
        self.assertEqual(user.cart.get('items')[1].get('name'), 'testdrink2')
        self.assertEqual(user.cart.get('items')[1].get('Matcha'), 9)
        
        orderItem3 = {
            "name": "testdrink3",
            "Matcha": 10,
            "Chocolate": -2
        }
        add_item_to_cart(user, orderItem3)
        self.assertEqual(user.cart.get('items')[2].get("Matcha"), 9)
        self.assertEqual(user.cart.get('items')[2].get("Chocolate"), 1)

    def test_place_order(self):
        print("Place order tests...")
        user = UserAccount.objects.get(email='test@dansfrappes.com')
        user.funds = 999.99
        user.save()
        orderItem1 = {
            "name": "testdrink",
            "milk": "Oat",
            "Chocolate": 5
        }
        user = UserAccount.objects.get(email='test@dansfrappes.com')
        place_order(user)
        self.assertEqual(len(user.cart.get('items')), 0)
        self.assertEqual(len(get_unfulfilled()), 1)

    def test_funds(self):
        print("Money management tests...")
        user = UserAccount.objects.get(email='test@dansfrappes.com')
        user.funds = 1000
        user.save()
        orderItem1 = {
            "name": "testdrink",
            "milk": "Oat",
            "Chocolate": 5
        }
        
        expectedCost = 5 * Ingredient.objects.get(name="Chocolate").buy_cost * other_markup + MilkIngredient.objects.get(name="Oat").buy_cost * milk_markup
        
        user = UserAccount.objects.get(email='test@dansfrappes.com')
        add_item_to_cart(user, orderItem1)
        initialFunds = UserAccount.objects.get(store=True).funds
        
        self.assertAlmostEqual(make_summary(user).get('total'), expectedCost, 2)
        
        # Place the order then check if the funds were correctly added / subtracted
        place_order(user)
        
        self.assertAlmostEqual(user.funds, 1000 - expectedCost, 2)
        self.assertAlmostEqual(UserAccount.objects.get(store=True).funds, initialFunds + expectedCost, 2)

