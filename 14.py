import time

memo = {}

def find_sequence(n):
    if not n in memo:
        if n == 1:
            memo[n] = 1
        if n % 2 == 0:
            memo[n] = find_sequence(n // 2) + 1
        else:
            memo[n] = find_sequence(3 * n + 1) + 1
    return memo[n]



print("Start time: ", time.strftime("%H:%M:%S"))

max_lenth = 0
starting_element = 0
count = 0
for i in range(1, 1000000):
    count = find_sequence(i)
    if not i % 10000:
        check = 1
    if count > max_lenth:
        max_lenth, starting_element = count, i

print(starting_element, max_lenth)

print("Finish time: ", time.strftime("%H:%M:%S"))