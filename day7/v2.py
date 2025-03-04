import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def safe_division(numbers, divisor):
    results = []
    
    for num in numbers:
        try:
            result = divisor / num
            results.append(round(result, 4)) 
        except ZeroDivisionError:
            logging.error(f"Error: Division by zero encountered for number {num}")
    
    return results
numbers = [1, 2, 0, 3, 0]
divisor = 1  
output = safe_division(numbers, divisor)
print(output)