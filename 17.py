def remove_junk(text):
    for junk_char in " -":
        new_text = text.replace(junk_char, '')
    return new_text

def transform_into_words(number):
    dict_n = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", \
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", \
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    dict_n2  = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    number_str = str(number)
    if len(number_str) > 3:
        thousends = number_str[-4]
    else:
        thousends = 0
    if len(number_str) > 2:
        houndreds = number_str[-3]
    else:
        houndreds = 0
    if len(number_str) > 1:
        tens = number_str[-2]
    else:
        tens = '0'
    digits = number_str[-1]

    number_in_words = ""
    if int(thousends):
        number_in_words += dict_n[int(thousends)] + "thousand"
    if int(houndreds):
        number_in_words += dict_n[int(houndreds)] + "hundred"
    if (int(houndreds) or int(thousends)) and (int(digits) or int(tens)):
        number_in_words += "and"
    if tens >= '2':
        number_in_words += dict_n2[int(tens) - 2]
        if int(digits):
            number_in_words+= "-"
        number_in_words += dict_n[int(digits)]
    elif tens >= '1':
        number_in_words += dict_n[int(digits) + 10]
    else:
        number_in_words += dict_n[int(digits)]
    
    return number_in_words

sum = 0

#print(transform_into_words(4021))

f = open("D:\\numbers to letters.txt", 'w')

for i in range(1, 1000 + 1):
    number_str = remove_junk(transform_into_words(i))
    f.write(number_str)
    f.write("\n")
    sum += len(number_str)

f.close()


print(sum)


