import sys
from utils import calculator,validator
print("Welcome to the Mathematical Expression Validator and Calculator!")
user_input=input("Enter a mathematical expression (or 'exit' to quit):")
if user_input=='exit':
    sys.exit()
else:
    user_input=input("Enter a mathematical expression (or 'exit' to quit):")
k=calculator.is_valid_expression(user_input)
if k:
    v=validator.calculate(user_input)
print(f"The result is:{v}")