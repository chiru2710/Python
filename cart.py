

#Available products
products = {
    1: {"name": "Apple", "price": 30},
    2: {"name": "Banana", "price": 10},
    3: {"name": "Mango", "price": 50},
    4: {"name": "Orange", "price": 20}
}

cart = {}  # Your shopping cart dictionary

#  Display the main menu
def show_menu():
    print("\n====== SHOPPING CART MENU ======")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove Product")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

# Show available products
def show_products():
    print("\nAvailable Products:")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ₹{info['price']}")

# Add item to cart
def add_to_cart():
    try:
        pid = int(input("Enter product ID to add: "))
        qty = int(input("Enter quantity: "))
        if pid in products:
            cart[pid] = cart.get(pid, 0) + qty
            print(f" Added {qty} x {products[pid]['name']} to cart.")
        else:
            print(" Product ID not found.")
    except ValueError:
        print(" Invalid input. Enter numbers only.")

# Remove item from cart
def remove_from_cart():
    try:
        pid = int(input("Enter product ID to remove: "))
        if pid in cart:
            del cart[pid]
            print(" Product removed from cart.")
        else:
            print(" Product not in cart.")
    except ValueError:
        print(" Invalid input. Enter numbers only.")

#  View cart
def view_cart():
    print("\n Your Cart:")
    if not cart:
        print("Cart is empty.")
    else:
        total = 0
        for pid, qty in cart.items():
            name = products[pid]['name']
            price = products[pid]['price']
            cost = qty * price
            total += cost
            print(f"{name} x {qty} = ₹{cost}")
        print(f"\n Total Amount: ₹{total}")

#  Checkout
def checkout():
    print("\n Checkout Summary:")
    view_cart()
    print(" Thank you for shopping with us!")

# Main Program Loop
while True:
    show_menu()
    choice = input("Select an option (1-6): ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout()
        break
    elif choice == "6":
        print(" Exiting... Goodbye!")
        break
    else:
        print(" Invalid choice. Try again.")