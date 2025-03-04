def add_item(inventory, item, quantity, price): 
    """Adds a new item to the inventory or updates the quantity if it exists.""" 
    if item in inventory: 
        current_quantity, current_price = inventory[item] 
        inventory[item] = (current_quantity + quantity, current_price) 
    else: 
        inventory[item] = (quantity, price) 
 
def calculate_total_value(inventory): 
    """Calculates the total value of the inventory (quantity × price).""" 
    return sum(quantity * price for quantity, price in inventory.values()) 
inventory = { 
    "apple": (10, 0.5), 
    "banana": (20, 0.3) 
} 
add_item(inventory, "apple", 5, 0.5)   
add_item(inventory, "orange", 15, 0.4) 
print("Updated Inventory:") 
print(inventory) 
total_value = calculate_total_value(inventory) 
print("Total Value:", total_value) 