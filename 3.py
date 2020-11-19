import math

#Checking if number is prime
def find_smallest_prime_factor(number):

    upper_bound = int(math.sqrt(number)) + 1

    for i in range(2, upper_bound):
        if number % i == 0:
            return i

    return number


def find_largest_prime_factor(number):
    while True:
        smallest_factor = find_smallest_prime_factor(number)

        if smallest_factor < number:
            number //= smallest_factor
        else:
            return number


result = find_largest_prime_factor(600851475143)
print(result)