
# Sample menu data
menu_items = [
    {"id": 1, "name": "Pizza", "description": "Delicious cheese pizza with fresh toppings.", "price": 12.99},
    {"id": 2, "name": "Burger", "description": "1burger with lettuce and tomato.", "price": 8.99},
    {"id": 3, "name": "icecream", "description": "icecream with different flavour.", "price": 10.99}
]

# Cart to store items added by the user
cart = []

# Function to show menu and ask the user for a selection
def show_menu():
    print("Menu:")
    for item in menu_items:
        print(f"{item['id']}. {item['name']} - ${item['price']}\nDescription: {item['description']}\n")

    # Ask user for menu selection
    while True:
        try:
            item_id = int(input("Enter the item number to add to your cart (or 0 to finish): "))
            if item_id == 0:
                break
            item = next((item for item in menu_items if item['id'] == item_id), None)
            if item:
                add_to_cart(item)
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to add item to the cart
def add_to_cart(item):
    cart.append(item)
    print(f"Added {item['name']} to your cart.")

# Function to view cart
def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your Cart:")
        total_amount = 0
        for item in cart:
            print(f"- {item['name']} - ${item['price']}")
            total_amount += item['price']
        print(f"Total: ${total_amount:.2f}")

# Function to place an order
def place_order():
    if not cart:
        print("Your cart is empty. Please add items before checking out.")
        return

    name = input("Enter your name: ")
    address = input("Enter your delivery address: ")

    print(f"\nOrder placed by {name} to the address: {address}")
    total_amount = sum(item['price'] for item in cart)
    print(f"Total amount: ${total_amount:.2f}")

    print("\nOrder details:")
    for item in cart:
        print(f"- {item['name']} - ${item['price']}")

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

