#Tuple---Tuple items are ordered,
#  unchangeable, and allow duplicate values.

# mytuple = ("apple", "banana", "cherry","banana", "cherry", "apple")
# print(mytuple)
# print(len(mytuples))

# tuple1 = ("abc", 34, True, 40, "male")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# print(tuple1)
# print(tuple2)
# print(tuple3)

#Access Tuple Items--

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])  #1st way
# print(thistuple[-4:-1]) #2nd way

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1]) #by range()

# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple") #conditional statement

#change in tuples Values--
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

#convert into a List:-
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple) # tuples
# print(y)  # list 

#add tuple to tuples--
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

#remove in tuples--
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

