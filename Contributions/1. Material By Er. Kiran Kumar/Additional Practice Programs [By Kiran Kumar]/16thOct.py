
# Function to Check a Given String is Palindrome or Not
def palindrome_checker(string):
    reverse = string[::-1]
    if string == reverse:
        return "Palindrome"
    else:
        return "Not a Palindrome"
check = palindrome_checker("mam")
print(check)



# Function to check a Given Number is Odd or Even

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
check = check_odd_even(5)
print(check)


# Function to return sum of two numbers 

def sum_two_num(num1,num2):
    return num1 + num2 
sum = sum_two_num(10,20)
print(sum)



# Function to return Substraction of Two Numbers 

def subtract_two_num(num1,num2):
    return num1 - num2 
subtract = subtract_two_num(20,5)
print(subtract)