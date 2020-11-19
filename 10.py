import math
import time

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    
    return True

print("Start time: ", time.strftime("%H:%M:%S"))
summ = 0
number = 2000000
for i in range(2, number):
    if isPrime(i):
        summ += i

print(summ)
print("Finish time: ", time.strftime("%H:%M:%S"))