#Create a generator that generates the squares of numbers up to some number N.

n = int(input())

square = (i ** 2 for i in range(n + 1))
 
for i in square:
    print(i)
    
    
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

even_numbers = (i for i in range(n + 1) if i % 2 == 0)

for i in even_numbers:
    print(i, end=' ')
    
#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for i in divisible(n):
    print(i)
    
#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

a, b = int(input()), int(input())

def squares2(a, b):
    for i in range(a, b + 1):
        yield i ** 2
        
        
#Implement a generator that returns all numbers from (n) down to 0.

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(n):
    print(num)