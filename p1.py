#nearst number to 0
def closest_to_zero(lis):
    if not lis:
        return None  
    
    closest = lis[0]  

    for num in lis:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    
    return closest
numbers = [-10, 3, 5, -2, 2, -1, 1]
print("Closest to zero:", closest_to_zero(numbers))