# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

print(1, '\n')

import re 


with open("row.txt") as f:
    data = f.read()


matches = re.findall(r"a.*b", data)
print(matches)


# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

print(2, '\n')

matches = re.findall("abb+|abbb+", data)
print(matches)


# Write a Python program to find sequences of lowercase letters joined with a underscore.

print(3, '\n')

matches = re.findall(r"[a-z]+_[a-z]+", data)
print(matches)


# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

print(4, '\n')


matches = re.findall(r"[A-Z]+[A-Z]+[a-z]+", data)
print(matches)


# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

print(5, '\n')


matches = re.findall(r"a.*b$", data)
print(matches)


# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

print(6, '\n')

matches = re.compile(r"[., ]")
result  = matches.sub(':', data)
print(result)


# Write a python program to convert snake case string to camel case string.

print(7, '\n')


matches = re.findall(".*", data)

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_case_string = "hello_world_python"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)


# Write a Python program to split a string at uppercase letters.

print(8, '\n')


matches = re.findall(".*", data)

def split_at_uppercase(input_string):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return result

for i in matches:
    print(split_at_uppercase(i))

f.close()


# Write a Python program to insert spaces between words starting with capital letters.

print(9, '\n')


with open("row.txt") as f:
    data = f.read()

matches = re.findall("[A-Z]+.*", data)

for match in matches:
    print(match, end=" ")


array = ["AnimalsWorldAreaHelloWorldGoodThingOverThinking", "SeasonWinterSpringAutumnSummer"]
result  = ' '
for element in array:
    for i in element:
        if i>='A' and i <='Z':
            result+='_'
        result+=i
print(result)


# Write a Python program to convert a given camel case string to snake case.

print(10, '\n')


def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case_string)
    snake_case_string = snake_case_string.lower()
    return snake_case_string

with open("row.txt") as f:
    data = f.read()

snake_case_data = camel_to_snake(data)

print(snake_case_data)





