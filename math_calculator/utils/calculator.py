def calculate(expression: str) -> float:
    try:
        k=eval(expression)
        return k
    except Exception as e:
        print(e)

