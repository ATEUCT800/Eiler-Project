import math

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    
    return True

count = 0
i = 1
while count < 10001:
    i += 1
    if isPrime(i):
        count += 1

print("{0} prime number is: {1}".format(count, i))