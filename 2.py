fibonachi_list = [1,2]
sum_of_fibonachi = 2

while sum(fibonachi_list) < 4e6:
    fibonachi_list[0], fibonachi_list[1] = fibonachi_list[1], sum(fibonachi_list)
    if fibonachi_list[1] % 2 == 0:
        sum_of_fibonachi += fibonachi_list[1]
print(sum_of_fibonachi)
