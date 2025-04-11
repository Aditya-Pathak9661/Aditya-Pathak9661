# Restaurant Order System

print("Welcome to aditya foodie's!")
print("\nMenu:")
menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 200,
    "Fries": 80,
    "Coke": 50
}

for item, price in menu.items():
    print(f"{item}: ₹{price}")

# Taking order
order = input("\nEnter the items you'd like to order, separated by commas: ").split(',')

# Calculate total
total = 0
for item in order:
    item = item.strip().capitalize()
    if item in menu:
        total += menu[item]
        
    else:
        print(f"Sorry, we don't have {item}.")
        print(f"please order some other item of {menu} ,sepearte with commas")
    
# Applying conditions
if total > 500:
    discount = 0.1 * total
    total -= discount
    print(f"\nYou have a discount of ₹{discount:.2f} for orders above ₹500!")

delivery_charge = 0
if total < 200:
    delivery_charge = 50
    total += delivery_charge
    print("\nA delivery charge of ₹50 has been added for orders below ₹200.")

# Display total
print(f"\nYour total bill is ₹{total:.2f}")
if delivery_charge > 0:
    print(f"(Including ₹{delivery_charge} delivery charge)")
print("\nThank you for ordering with us!")