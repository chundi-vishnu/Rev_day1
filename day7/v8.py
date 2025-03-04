import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# Example usage
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_numbers = find_primes(start, end)
print(f"Prime numbers between {start} and {end}: {prime_numbers}")