# Write a Python program with builtin function to multiply all the numbers in a list
def multiply_list(array):
    s = 1
    for i in array:
        s *= i
    return s

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def sumofletters(letter):
    uppercase = 0
    lowercase = 0
    for i in letter:
        if i>='A' and i<='Z':
            uppercase+=1
        elif i>='a' and i<='z':
            lowercase+=1
    result = [lowercase, uppercase]
    return result

# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def palindrom(letter):
    if letter == letter[::-1]:
        return f"the word {letter} is palindrom"
    else:
        return f"the word {letter} isn't palindrom"
    
# Write a Python program that invoke square root function after specific milliseconds.
def squareroot():
    import time
    import math
    x = int(input("Input the value: "))
    y = int(input("Input the miliseconds: "))
    y=y/1000
    time.sleep(y)
    return f"Square root of {x} after {y} miliseconds is {math.sqrt(x)}"

# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true_elements(tuple_data):
    boolean =  True
    for i in tuple_data:
        if i != True:
            boolean = False

    if boolean:
        return True
    else:
        return f"elements of tuple is different"