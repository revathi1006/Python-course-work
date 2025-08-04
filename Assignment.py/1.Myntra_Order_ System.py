# Myntra Order System

# Input Section
order_id = int(input("Enter Order ID: "))
customer_name = input("Enter Customer Name: ")
total_amount = float(input("Enter Total Order Amount: "))

# List
items_ordered = [item.strip() for item in input("Enter Items Ordered (comma-separated): ").split(',')]

# Tuple
delivery_address = (
    input("Enter Delivery City: "),
    input("Enter Delivery Pincode: ")
)

# Float
discount_applied = float(input("Enter Discount Percentage: "))

# Set
payment_methods = set(pm.strip() for pm in input("Enter Payment Methods Used (comma-separated): ").split(','))

# Dictionary
brand = input("Enter Favorite Brand: ")
category = input("Enter Preferred Category: ")
myntra_info = {
    "Brand": brand,
    "Category": category
}

# Output Section
print("\n--- Myntra Order Summary ---")

# 1. Using Comma Separation
print("Order ID, Customer Name, Total:", order_id, customer_name, total_amount, sep=',')

# 2. Using Percentage Formatting
print("Discount Applied: %.2f%%" % discount_applied)

# 3. Using f-strings
print(f"Customer Name: {customer_name}")
print(f"Items Ordered: {items_ordered}")
print(f"Delivery Address: {delivery_address[0]} - {delivery_address[1]}")
print(f"Payment Methods Used: {payment_methods}")

# 4. Using .format() method
print("Myntra Preferences: Brand - {}, Category - {}".format(
    myntra_info["Brand"], myntra_info["Category"]
))



'''Enter Delivery City: Hyd
Enter Delivery Pincode: 500081
Enter Discount Percentage: 15
Enter Payment Methods Used (comma-separated): UPI,Wallet
Enter Favorite Brand: Roadster
Enter Preferred Category: Women's Clothing

--- Myntra Order Summary ---
Order ID, Customer Name, Total:,200,Revathi,2000.5
Discount Applied: 15.00%
Customer Name: Revathi
Items Ordered: ['Kurti', 'jeans', 'shoes']
Delivery Address: Hyd - 500081
Payment Methods Used: {'Wallet', 'UPI'}
Myntra Preferences: Brand - Roadster, Category - Women's Clothing'''