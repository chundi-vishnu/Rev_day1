def calculate_total_sales(sales_data): 
    return {product: sum(sales) for product, sales in sales_data.items()} 
sales_data = { 
    "Product A": [100, 200, 150], 
    "Product B": [50, 75, 100], 
    "Product C": [300, 250, 400] 
} 
total_sales = calculate_total_sales(sales_data) 
print(total_sales)