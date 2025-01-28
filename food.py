import mysql.connector
from mysql.connector import Error

# Database connection parameters
username = 'root'
password = '186707'
host = 'localhost'
database = 'food_delivery'

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
    return None

# Retrieve menu items from the database
def get_menu_items():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM menu_items"
            cursor.execute(query)
            menu_items = cursor.fetchall()
            return [
                {"id": item[0], "name": item[1], "description": item[2], "price": item[3]}
                for item in menu_items
            ]
        except Error as e:
            print(f"Error retrieving menu items: {e}")
            return []
        finally:
            cursor.close()
            connection.close()
    else:
        return []

# Insert user into the database
def insert_user(name, phone_number, address):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO users (name, phone_number, address) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, phone_number, address))
            connection.commit()
            return cursor.lastrowid  # Return the ID of the newly inserted user
        except Error as e:
            print(f"Error inserting user: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
    return None

# Insert order into the database
def insert_order(user_id, total_amount, cart):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            # Insert the order into the orders table
            query = "INSERT INTO orders (user_id, total_amount) VALUES (%s, %s)"
            cursor.execute(query, (user_id, total_amount))
            order_id = cursor.lastrowid  # Get the ID of the newly inserted order

            # Insert each item in the cart into the order_items table
            for item in cart:
                item_query = "INSERT INTO order_items (order_id, menu_item_id, quantity) VALUES (%s, %s, %s)"
                cursor.execute(item_query, (order_id, item['id'], item['quantity']))

            connection.commit()  # Commit the transaction
            print("Order inserted into database successfully!")
        except Error as e:
            print(f"Error inserting order: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")

# Cart to store items added by the user
cart = []

# Function to show menu and ask the user for a selection
def show_menu():
    menu_items = get_menu_items()  # Retrieve menu items from the database
    if not menu_items:
        print("No menu items found.")
        return

    print("Menu:")
    for item in menu_items:
        print(f"{item['id']}. {item['name']} - ${item['price']:.2f}\nDescription: {item['description']}\n")

    # Ask user for menu selection
    while True:
        try:
            item_id = int(input("Enter the item number to add to your cart (or 0 to finish): "))
            if item_id == 0:
                break
            item = next((item for item in menu_items if item['id'] == item_id), None)
            if item:
                quantity = int(input(f"Enter quantity for {item['name']}: "))
                cart.append({"id": item['id'], "name": item['name'], "price": item['price'], "quantity": quantity})
                print(f"Added {quantity} of {item['name']} to your cart.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to view cart
def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        total_amount = 0
        for item in cart:
            print(f"- {item['name']} (x{item['quantity']}) - ${item['price']:.2f} each")
            total_amount += item['price'] * item['quantity']
        print(f"Total: ${total_amount:.2f}")
    return total_amount

# Function to place an order
def place_order():
    if not cart:
        print("Your cart is empty. Please add items before checking out.")
        return

    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your delivery address: ")

    # Insert user and get user ID
    user_id = insert_user(name, phone_number, address)
    if user_id is None:
        print("Failed to create user. Order cannot be placed.")
        return

    total_amount = view_cart()  # Get the total amount from the cart

    # Insert order into database
    insert_order(user_id, total_amount, cart)

    # Clear the cart after placing the order
    cart.clear()
    print("\nThank you for your order! It has been placed successfully.\n")

# Main Program Flow
while True:
    print("\nWelcome to the Food Delivery App!")
    print("1. View Menu")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    try:
        choice = int(input("Please enter your choice: "))

        if choice == 1:
            show_menu()
        elif choice == 2:
            view_cart()
        elif choice == 3:
            place_order()
        elif choice == 4:
            print("Thank you for visiting! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")