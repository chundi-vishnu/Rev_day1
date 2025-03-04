n=50
prime_numbers = {num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))}

# Print the set of prime numbers
print(prime_numbers)