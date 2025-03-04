def read_write_text():
    with open(r'C:\Users\HP\rev_day2\day3\vishnu.txt', "r") as file:
        content = file.read()
    print(content)
    
    with open("C:/Users/HP/rev_day2/day3/priya.txt", "a") as file:
        file.write(content)

# Example usage
read_write_text()
