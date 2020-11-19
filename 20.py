from math import factorial

NUMBER = 100

def find_sum_fact(n):

    num_str = str(factorial(n))
    return sum(int(c) for c in num_str)

print(find_sum_fact(NUMBER))