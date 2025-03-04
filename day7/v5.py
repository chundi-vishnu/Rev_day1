import re 
def validate_password(password): 
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$" 
    return bool(re.match(pattern, password)) 
password = "Password1!" 
print(validate_password(password)) 