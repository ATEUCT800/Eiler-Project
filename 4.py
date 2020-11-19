
#Reversing text
def reverse(text):
    return text[::-1]

#Checking if number is polindrome
def is_polindrome(number):
    
    text_number = str(number) #convert number into string

    return text_number == reverse(text_number)


bigest_polindrome = 100 * 100 #starting point

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_polindrome(i * j) and i * j > bigest_polindrome:
            bigest_polindrome = i * j

print(bigest_polindrome)
