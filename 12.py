import math

def count_dividers(number):
    count = 0

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            count += 1
    count *= 2

    return count

i = 0
count = 0
triangle = 0

while count < 500:
    i += 1
    triangle += i
    count = count_dividers(triangle)

print("Number {0} has {1} dividers".format(triangle, count))