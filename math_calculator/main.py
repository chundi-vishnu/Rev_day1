import sys
from utils import calculator
from utils import validator
print("Welcome to the Mathematical Expression Validator and Calculator!")
while True:
    user_input=input("Enter a mathematical expression (or) 'exit' to quit:")
    k=validator.is_valid_expression(user_input)
    if k:
        v=calculator.calculate(user_input)
        print(v)
    elif not k:
        print("Not a valid expression")
    elif user_input=='exit':
        sys.exit(0)
