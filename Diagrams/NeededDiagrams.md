# Needed Diagrams

Diagrams are needed for the following use cases:
1. Customer makes an account
2. Customer places an order
3. Customer adds order to favorites
4. User edits account details
5. Employees handle an order
    * Make
    * Give to customer
6. Manager orders inventory
7. Manager pays employees


# Use Case Diagrams

## Customer Makes an Account
Entry conditions:
1. Customer wants an account with Dan's Frappes

Exit conditions:
1. Customer exits account creation or completes the form

Event flow:
1. Customer clicks create account link
2. System displays new account form
3. Customer enters email, name, password, and birthday, then clicks create new account
4. Information is sent to the server, and database is updated with new account information
    * Password is sent securely

## Customer Places an Order
Entry conditions:
1. Customer has logged in to the website
2. Customer wants to order something

Exit conditions:
1. Customer clicks place order and sucessfully pays
2. OR customer clears their order

Event flow:
1. Customer views the menu page
2. Customer clicks on a menu item to view details
3. System displays information on the item including customizable components
    * If an ingredient is out of stock, that will be displayed here
4. The customer customizes an order, then clicks add to order
5. The item is sent to the server and added to the customer's current order
    * This saves partial orders if the customer logs in from another device
6. Steps 2-5 are repeated for as many items as the customer would like
7. The customer clicks the view order button
8. The server displays the customers full order and the cost
9. If the customer doesn't have enough money, an add funds button is shown
10. If the customer does have enough money, they click pay
11. The server adds the order to the queue
12. The customer's current order is cleared

## Customer Saves an Order
Entry conditions:
1. Customer has signed in
2. Customer has placed an order previously

Exit conditions:
1. Customer saves or exits the add to favorites popup

Event flow:
1. Customer views their account details
2. Server displays details, along with a list of recently ordered items
3. Customer selects an item, then clicks add to favorites
4. Customer enters a name for the item, then clicks save
5. Server adds order with name to customer database

## Employee Makes an Order
Entry conditions:
1. Employee has signed in

Exit conditions:
1. Employee clicks that an order is fulfilled
    * OR Employee clicks cancel order

Event flow:
1. Server presents the employee with all unfulfilled orders in a queue
2. Employee clicks on an order to view it in more detail
3. Employee clicks "mark as complete" button to finish order
4. Server marks order as complete and moves it to the list of completed orders

## Employee Gives an Order to a Customer
Entry conditions:
1. Order has been previously made
2. Customer has arrived for pickup, and has given the employee the name on the order

Exit conditions:
1. Employee clicks "mark as complete"

Event flow:
1. Server presents cashier with a list of fulfilled orders sorted by name
2. Employee clicks on the correct order
3. Employee clicks "mark as complete"
4. Server removes order from the list
5. Server updates the transaction history of the customer to show that the order was picked up

## Manager Pays Employees
Entry conditions:
1. Manager has signed in

Exit conditions:
1. Manager clicks pay employees

Event flow:
1. Manager opens employee view
2. Server displays all employees and the hours they worked
3. Manager clicks pay employees
4. Server removes money from the store account and adds money to each employee account
5. Each employee's hours worked field is reset to 0 

## Manager Orders Inventory
Entry conditions:
1. Manager has signed in
2. Manager needs more inventory

Exit conditions:
1. Manager clicks the order button or the cancel button

Event flow:
1. Manager clicks on view inventory
2. Server displays a list of all current inventory, with an empty field next to each
3. Manager enters the number to order of each ingredient, then clicks order
4. Server subtracts money from manager's account, and adds selected items to the inventory database

## User Edits Profile
Entry conditions:
1. User has signed in

Exit conditions:
1. User clicks the save button or the cancel button

Event flow:
1. User views their account details
2. Server displays account info
3. User clicks edit account button
4. Server loads a form with the account information
5. User edits the form and clicks submit
6. Server updates database information
7. User is redirected to the account details page