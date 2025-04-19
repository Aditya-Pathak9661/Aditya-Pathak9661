# Loop through a List--
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

#loop through the Index Numbers--
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# Looping Using List Comprehension ---
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# #Example--
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist) #without list comprehension

#with list comprehension --
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

#Syntax --> newlist = [expression for item in iterable if condition == True]


#condition --
# newlist = [x for x in fruits if x != "apple"]

# newlist = [x for x in range(10)]
# print(newlist)

# Expression --
# newlist = [x.upper() for x in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]
# newlist = ['hello' for x in fruits]
# print(newlist)


#sorting -->
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

#sort descending-
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

#reverse order--
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist) # it only reverse your given list order. 

#Customize sort function --> it is based on nearest number
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist) #nearest in all , then next...

#Case sensitive Sorting--
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist) #base on Capital or Small of first letter

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)  # based on alphabetical order a - b - c...

# Copy a List--


# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

'''You cannot copy a list simply by typing list2 = list1,
because: list2 will only be a reference to list1,
and changes made in list1 will automatically 
also be made in list2'''

# Use this --
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#use the Slice Operator -->
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist) # from starting to end(copied)

# Python - Join Lists

# list1 = ["a", "b", "c"] #by useing concatenate
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

#by using append()-
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

#by using extend()-
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

