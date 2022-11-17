# # Write a function to take in a sentence and assign a numeric value to each letter.
# # No two letters should have the same numeric value, and each letter should have a
# # dedicated value (so that the same letter does not have two numeric values).

# def ranking(sentence):
#     number = {}
#     indi = []
#     z = 0
#     for i in sentence:
#         if i.

# import re

# with open('regex_test.txt') as f:
#     data = f.read()
#     print(data)

# pattern = re.compile(r"^([A-Z]([a-z]+|.)\s*){2,3}$")    
# match = pattern.findall(data)

# print(match)


# Week 3: Day 3 - Whiteboard

# Fizz Buzz
# Write a function to that takes one parameter
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number

# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         print("FizzBuzz")
#         return
#     if input % 3 == 0:
#         print("Fizz")

#     elif input % 5 == 00:
#         print("Buzz")

#     else:
#         print(input)

# fizz_buzz(22)


# Python3 program to
# Check if the string is pangram

  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")
