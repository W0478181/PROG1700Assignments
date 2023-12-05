#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Import Modules
import sys
import re
#Variables
tries = 0
#Dictionary
customers = {
    1: {"FirstName": "Alice", "LastName": "Byers", "Contact": "123-456-7890", "Orders": []},
    2: {"FirstName": "Bob", "LastName": "Rhynolds", "Contact": "098-765-4321", "Orders": []}
}
#Functions
#Users have 3 attempts anytime they must input information, If there are 3 invalid attempts they will get a message and program will shut down.
def attempts():
    global tries
    tries += 1
    if tries < 3:
        print("\nInvalid input. Please try again.")
    if tries == 3:
        print("\nToo many failed attemps please try again later.")
        sys.exit()
#Option to add Customers to dictionary and auto generate ID, Names can only be letters and Contact may only be 10 digits and will automatically be spaced.
def add_customer(customers):
    new_customer_id = len(customers) + 1
    FirstName = input("\nEnter new customers First Name:")
    if not FirstName.isalpha():
        attempts()
        return
    LastName = input("\nEnter new customers Last Name:")
    if not LastName.isalpha():
        attempts()
        return
    Contact = input("\nEnter new customers Phone Number:")
    if not Contact.isdigit() and len(Contact) != 10:
        attempts()
        return
    Contact = f"{Contact[:3]}-{Contact[3:6]}-{Contact[6:]}"
    customers[new_customer_id] = {"FirstName": FirstName, "LastName": LastName, "Contact": Contact,"Orders": []}
    print("Customer added successfully")      
#Option to add Orders to Customers and will generate a Order ID starting at 1 for each Customer, Unit Price will automatically put a $ before price.
def add_order(customers):
    while True:
        try:
            search_cust_id = int(input("Enter Customer ID to place order: "))
        except ValueError:
                attempts()
                continue
        if search_cust_id in customers:
            customer = customers[search_cust_id]
            customer_Orders = customer.get("Orders", [])
            order_id = len(customer_Orders) + 1
            print(f'\nEnter order details for {customer["FirstName"]} {customer["LastName"]}| Customer ID: {search_cust_id}| Order ID: {order_id}\n')
            product_Name = input("\nWhat is the Product Name:")
            if not re.match("^[a-zA-Z0-9\s]*$", product_Name):
                attempts()
                return
            unit_price = input("\nWhat is the Price of the item:")
            try:
                unit_price = float(unit_price)
            except ValueError:
                attempts()
                return
            quantity = input("\nWhat is the quantity of the order:")
            if not quantity.isdigit():
                attempts()
                return
            total_spent = (unit_price * float(quantity))
            unit_price = f"${unit_price}"
            customer_Orders.append({'Order ID': order_id, 'Product Name': product_Name, 'Unit Price': unit_price, 'Quantity': quantity, 'Total Spent': total_spent})
        else:
            attempts()
            continue
       
        customers[search_cust_id].update({'Orders': customer_Orders})
        print("Order added successfully")
        break
#Users can search dictionary for specific user reports, Will update if used before and after Orders and Customers are created.
def search_reports():
    while True:
        try:
            search_cust_id = int(input("Enter Customer ID to find customer info: "))
        except ValueError:
            attempts()
            continue
        if search_cust_id in customers:
            customer = customers[search_cust_id]
            total_spent = 0
            print(f'\nCustomer ID: {search_cust_id}')
            for key, value in customer.items():
                if key == 'Orders':
                    print(f'{key}:')
                    for order in value:
                        print(f"Order ID {order['Order ID']}\nProduct Name: {order['Product Name']}\n{order['Quantity']} units at {order['Unit Price']}")
                        total_spent += order.get('Total Spent', 0)  #Update total spent for each order
                    print(f"Total Spent by Customer: ${round(total_spent, 2)}")
                else:
                    print(f'{key}: {value}')
            break
        else:
            attempts()
            continue
#Users can search dictionary for all user reports, Will update if used before and after Orders and Customers are created.        
def all_reports():
    for cust_id, cust_info in customers.items():
        print('\nCustomer ID:', cust_id)
        total_spent = 0
        for key, value in cust_info.items():
            if key == 'Orders':
                print(f'{key}:')
                for order in value:
                    print(f"Order ID {order['Order ID']}\nProduct Name: {order['Product Name']}\n{order['Quantity']} units at {order['Unit Price']}")
                    total_spent += order.get('Total Spent', 0)
                print(f"Total Spent by Customer: ${round(total_spent, 2)}")
            else:
                print(f'{key}: {value}')
#Menu to choose what Users would like to do.
while True:
    user_input = input("""
        Order and Customer Management System Menu
        Press the corresponding number with your choice
       
        1. Add Customer
       
        2. Place Order
       
        3. Generate Customer Report
       
        4. Generate All Customer Reports
       
        5. Exit\n
        :""")
    #How Users input will pull functions
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            add_customer(customers)
        elif user_input == 2:
            add_order(customers)
        elif user_input == 3:
            search_reports()
        elif user_input == 4:
            all_reports()          
        elif user_input == 5:
            print('Thank You, Goodbye')
            sys.exit()
        else:
            attempts()    
    else:
        attempts()