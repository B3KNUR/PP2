#ex1
mylist = ["apple", "banana", "cherry"]

#ex2
thislist = ["apple", "banana", "cherry"]
print(thislist)

#ex3
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#ex4
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#ex5
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#ex6
list1 = ["abc", 34, True, 40, "male"]

#ex7
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#ex8
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#ex9
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#ex10
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#ex10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#ex11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#ex12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#ex13
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#ex14
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#ex15
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#ex16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#ex17
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#ex18
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#ex19
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#ex20
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#ex21
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#ex22
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ex23
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#ex24
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#ex25
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#ex26
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#ex27
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#ex28
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#ex29
thislist = ["apple", "banana", "cherry"]
del thislist

#ex30
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#ex31
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
#ex32
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#ex33
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#ex34
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#ex35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#ex36
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#ex37
newlist = [x for x in fruits if x != "apple"]

#ex38
newlist = [x for x in fruits]

#ex39
newlist = [x for x in range(10)]

#ex40
newlist = [x for x in range(10) if x < 5]

#ex41
newlist = [x.upper() for x in fruits]

#ex42
newlist = ['hello' for x in fruits]


#ex43
newlist = [x if x != "banana" else "orange" for x in fruits]

#ex44
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#ex45
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#ex46
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#ex47
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#ex48
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#ex49
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#ex50
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#ex51
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#ex52
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#ex53
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#ex54
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#ex55
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#ex56
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#ex57
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''

