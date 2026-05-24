import random  # To generate an order number

# Sample Pizza Ordering System
print("Welcome to the Mom & Pop's Pizza Shop!")

# Display Menu
menu = {
    "small": 10,
    "medium": 15,
    "large": 20
}
topping_price = 2  # Price per topping
toppings_list = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon"]

# Helper Function to Display the Menu
def display_menu():
    print("\nMenu:")
    for pizza, price in menu.items():
        print(f"{pizza.capitalize()} Pizza: ${price}")
    print("\nAvailable Toppings ($2 each):")
    for topping in toppings_list:
        print(f"- {topping}")

# Function to Get Toppings
def get_toppings():
    selected_toppings = []
    print("\nAvailable Toppings:")
    for i, topping in enumerate(toppings_list, 1):
        print(f"{i}. {topping}")
    while True:
        choice = input("\nSelect a topping by number (or type 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(toppings_list):
            topping = toppings_list[int(choice) - 1]
            half_choice = input(f"Do you want {topping} on the (1) First Half, (2) Second Half, or (3) Whole Pizza? ").strip()
            if half_choice in ["1", "2", "3"]:
                half_mapping = {"1": "First Half", "2": "Second Half", "3": "Whole Pizza"}
                selected_toppings.append((topping, half_mapping[half_choice]))
                print(f"{topping} added to the {half_mapping[half_choice]} of your pizza.")
            else:
                print("Invalid choice for pizza half. Try again.")
        else:
            print("Invalid choice. Try again.")
    return selected_toppings

# Function to Get Customer Information
def get_customer_info():
    print("\nCustomer Information:")
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()
    email = input("Enter your email address: ").strip()
    address = input("Enter your delivery address: ").strip()
    pickup_or_delivery = input("Will it be Pickup or Delivery? (Enter 'Pickup' or 'Delivery'): ").strip().lower()
    
    # Return customer info as a dictionary
    customer_info = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "pickup_or_delivery": pickup_or_delivery
    }
    
    return customer_info

# Main Order Function
def take_order():
    total_cost = 0
    order_details = []
    
    # Get Customer Information
    customer_info = get_customer_info()
    
    # Generate an order number
    order_number = random.randint(1000, 9999)  # Random order number between 1000 and 9999
    
    while True:
        display_menu()
        choice = input("\nWhich pizza would you like to order? (Small/Medium/Large): ").strip().lower()
        if choice in menu:
            toppings = get_toppings()
            topping_cost = len(toppings) * topping_price
            pizza_cost = menu[choice]
            total_cost += pizza_cost + topping_cost
            order_details.append({
                "size": choice.capitalize(),
                "toppings": toppings,
                "cost": pizza_cost + topping_cost
            })
            print(f"\nYou ordered a {choice.capitalize()} pizza with {len(toppings)} topping(s). Total: ${pizza_cost + topping_cost}")
        else:
            print("Invalid choice. Please restart the system.")
        
        another = input("\nDo you want to add another pizza to your order? (yes/no): ").strip().lower()
        if another != "yes":
            break
    
    # Display Final Order with Customer Name and Order Number
    print("\nYour Order Summary:")
    for item in order_details:
        print(f"{item['size']} Pizza - ${item['cost']}")
        for topping, half in item['toppings']:
            print(f"  - {topping} on {half}")
    print(f"Grand Total: ${total_cost}")
    
    # Thank the customer and display the order number
    print(f"\nThank you for your order, {customer_info['name']}!")
    print(f"Your order number is: {order_number}")

# Run the Ordering System
take_order()
