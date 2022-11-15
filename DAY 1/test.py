# # Write a function to take in a sentence and assign a numeric value to each letter.
# # No two letters should have the same numeric value, and each letter should have a
# # dedicated value (so that the same letter does not have two numeric values).

# def ranking(sentence):
#     number = {}
#     indi = []
#     z = 0
#     for i in sentence:
#         if i.

import re

with open('regex_test.txt') as f:
    data = f.read()
    print(data)

pattern = re.compile(r"^([A-Z]([a-z]+|.)\s*){2,3}$")    
match = pattern.findall(data)

print(match)
