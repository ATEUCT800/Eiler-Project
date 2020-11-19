import time

def check_condition(a, b, c):
    if a < b and b < c:
        if a*a + b*b == c*c:
            return True
    return False

print("Start time: ", time.strftime("%H:%M:%S"))
number = 1000

for a in range(number):
    for b in range(a, number):
        c = number - a - b
        if check_condition(a, b, c):
            print(a, b, c, end = ' ')
            print("\nProduct = {0}".format(a * b * c))
            break

print("Finish time: ", time.strftime("%H:%M:%S"))