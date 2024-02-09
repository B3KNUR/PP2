#1 A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


#2 Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


#3 Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) / 2
    x = numheads - y
    return (int(x), int(y))


#4 You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]


#5 Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    
    for perm in perms:
        print(''.join(perm))


#6 Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse(s):
    sentence = list(map(str, s.split()))
    sentence.reverse()
    return sentence


#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


#8 Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    index_0 = False
    index_1 = False

    for num in nums:
        if num == 0 and not index_0:
            index_0 = True
        elif num == 0 and index_0 and not index_1:
            index_1 = True
        elif num == 7 and index_0 and index_1:
            return True
    
    return False


#9 Write a function that computes the volume of a sphere given its radius.

import math

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


#10 Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b


#11 Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(s):
    s1 = s[::-1]
    return (s == s1)

#12 Define a functino histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

def histogram(a):
    for x in a: print('*' * x)
    
    
#13 Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:

import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

guess_the_number()