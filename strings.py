#ex1
print("Hello")
print('Hello')

#ex2
a = "Hello"
print(a)

#ex3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#ex4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#ex5
a = "Hello, World!"
print(a[1])

#ex6
for x in "banana":
  print(x)
  
#ex7
a = "Hello, World!"
print(len(a))

#ex8
txt = "The best things in life are free!"
print("free" in txt)

#ex9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#ex10
txt = "The best things in life are free!"
print("expensive" not in txt)

#ex11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#ex12
b = "Hello, World!"
print(b[2:5])

#ex13
b = "Hello, World!"
print(b[:5])

#ex14
b = "Hello, World!"
print(b[2:])

#ex15
b = "Hello, World!"
print(b[-5:-2])

#ex16
a = "Hello, World!"
print(a.upper())

#17
a = "Hello, World!"
print(a.lower())

#ex18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#ex19
a = "Hello, World!"
print(a.replace("H", "J"))

#ex20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#ex21
a = "Hello"
b = "World"
c = a + b
print(c)

#ex22
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#ex23
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#ex24
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#ex25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#ex26
txt = "We are the so-called \"Vikings\" from the north."