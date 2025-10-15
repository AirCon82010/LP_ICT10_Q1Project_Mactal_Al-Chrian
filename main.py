from pyscript import display

# 🏁 Pit Stop Café (F1-themed restaurant)

# Basic Information
restaurant_name = "Pit Stop Café"
owner_name = "Team Principal: AC Mactal"
year_since = 2025

# Tax rate (optional)
tax_rate = 0.10

# Order types
has_delivery = True
is_dine_in = True
is_takeaway = True

# List of products
f1_foods = ["Racer Burger", "Speed Pasta", "Pit Fries"]
f1_drinks = ["Turbo Coffee", "Nitro Soda"]

# Tuple (Business hours)
business_hours = ("Monday - Sunday", "10:00 AM to 11:00 PM")

# Dictionary (Menu with prices)
menu = {
    "Racer Burger": 249.99,
    "Speed Pasta": 199.99,
    "Pit Fries": 99.99,
    "Turbo Coffee": 70.00,
    "Nitro Soda": 45.00
}

# Set (Allergens / track hazards)
track_hazards = {"Dairy", "Gluten", "Soy"}

# Display restaurant info
display(restaurant_name, target="name1")
display(owner_name, target="owner")
display(f"Since {year_since}", target="since")
display("🏎️ Menu Pricelist 🏁", target="heading1")

# Display menu items with prices
display(f1_foods[0], target="prod1")
display(f"₱{menu['Racer Burger']:.2f}", target="price1")

display(f1_foods[1], target="prod2")
display(f"₱{menu['Speed Pasta']:.2f}", target="price2")

display(f1_foods[2], target="prod3")
display(f"₱{menu['Pit Fries']:.2f}", target="price3")

display(f1_drinks[0], target="prod4")
display(f"₱{menu['Turbo Coffee']:.2f}", target="price4")

display(f1_drinks[1], target="prod5")
display(f"₱{menu['Nitro Soda']:.2f}", target="price5")

# Business hours
display(f"Open: {business_hours[0]} • {business_hours[1]}", target="openingHours")

# Order availability
if has_delivery:
    display("Delivery Available 🛵", target="orderType")
else:
    display("Dine-in Only", target="orderType")
