summ = int(0)
for i in range (1,1000):
	if not(i % 3 and i % 5):
		#print(i, end = ' ')
		summ += i
print(summ)

