
# Recursive function to calculate sum of natural numbers
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)


# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test the functions
numbers = [5, 10, 18]

for n in numbers:
    print("\nNumber:", n)
    print("Sum of natural numbers:", sum_n(n))
    print("Factorial:", factorial(n))
