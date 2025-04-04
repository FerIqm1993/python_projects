# Prime Numbers Exercise
# Create a list of random numbers
import random

# Number of elements in the initial list
n = 100
random_numbers = [random.randint(1, n) for i in range(n)]
random_numbers.sort()

# Display the original list
print("Original number list:", random_numbers)
print("Original number count:", len(random_numbers))

# Function to filter prime numbers
def filter_primes(random_numbers):
    prime_list = []
    for number in random_numbers:
        if number % 2 != 0:
            prime_list.append(number)
    prime_list.sort()
    return prime_list

# Display both lists and the count of elements
print("List of prime numbers:", filter_primes(random_numbers))
print("Count of prime numbers:", len(filter_primes(random_numbers)))
