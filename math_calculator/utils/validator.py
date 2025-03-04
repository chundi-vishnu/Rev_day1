import re
def is_valid_expression(expression:str)->bool:
    pattern = r'^[\d\-+*/() ]+$'
    return bool(re.fullmatch(pattern, expression))
