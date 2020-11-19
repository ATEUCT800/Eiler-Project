def sum_of_sqr(number):
    sum = 0
    for i in range(number + 1):
        sum += i * i
    return sum
    
def sqr_of_sum(number):
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum * sum

print(sqr_of_sum(100) - sum_of_sqr(100))