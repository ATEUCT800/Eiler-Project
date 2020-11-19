from math import sqrt
import time

def d(n):
    return sum(i for i in range(1, n//2 + 1) if n % i == 0)

def sum_of_friend_number(number):
    #slow
    # return sum(a for a in range(number + 1) if d(a) < number and d(a) != a and d(d(a)) == a) 

    # this one is more then 2 times faster:
    sum = 0
    for a in range(number + 1):
        b = d(a)
        if b < number and b != a and d(b) == a:
            sum += a
    return sum


start_time = time.time()
print(sum_of_friend_number(10000))
print(f'Execution took: {(time.time() - start_time):{.2}f} sec')
