def find_count(number, power):
    result_str = str(number ** power)
    sum = 0
    for c in result_str:
        sum += int(c)
    return sum

print(find_count(2, 1000))