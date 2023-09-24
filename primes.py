"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes must be greater than 0.")

    list = []

    num = 2
    while number_of_primes > 0:
        if is_prime(num):
            list.append(num)
            number_of_primes -= 1
        num += 1

    return list


def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True
