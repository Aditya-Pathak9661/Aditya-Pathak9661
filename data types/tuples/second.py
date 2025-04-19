
#unpacking in python tuple-->

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

'''Note: The number of variables must
match the number of values in the tuple,
if not, you must use an asterisk to collect the
remaining values as a list.'''
#use of astrisk-->

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

#python - Loop Tuples -->
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

''' use the range() and len() functions to
 create a suitable iterable.'''

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

#while--
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

#join two tuples--

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

#Multiply Tuples--
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

