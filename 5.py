import time

def div_by_10(number):

    for i in range(20, 10, -1):
        if number % i != 0:
            return False

    return True

print(time.strftime('%H:%M:%S'))

max_number = 1

for i in range(11, 21):
    max_number *= i

for i in range(2520, max_number, 2520):
#for i in range(1, max_number):
    if div_by_10(i):
        print(i)
        break

print(time.strftime('%H:%M:%S'))