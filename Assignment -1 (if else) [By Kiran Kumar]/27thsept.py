# Question - 87 
# Write a program to find the smallest among three numbers.

num1 = int(input("Enter number - 1 :"))
num2 = int(input("Enter number - 2 :"))
num3 = int(input("Enter number - 3 :"))

if (num1<num2) and (num1<num3):
    print(num1," is smallest")
elif (num2<num1) and (num2<num3):
    print(num2,"is smallest.") 
else:
    print(num3,"is samllest.")
    
    
    
# Question - 90
# Write a program to check whether a given character is vowel or consonant using nested if.

entered_character = input("Enter a character :").lower()
if entered_character == 'a':
    print("Vowel")
elif entered_character == 'e':
    print("Vowel")
elif entered_character == 'i':
    print("Vowel")
elif entered_character == '0':
    print("Vowel")
elif entered_character == 'u':
    print("Vowel")
else:
    print("Consonant")
   