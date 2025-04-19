#Sets in python --A set is a collection which is unordered,
#  unchangeable*, and unindexed.

# myset = {"apple", "banana", "cherry","cherry", "apple"}
# print(myset)

#true consider as 1, false consider as 0 --
# thisset = {"apple", "banana", "cherry", False, True, 0 , 1, 2, 12}
# print(thisset)

# print(len(thisset)) # true and false is 1, 0 respectively.

# set1 = {"abc", 34, True, 40, "male"} #set data is anything
# print(set1)

#access Items--
thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# print("banana" in thisset)

# thisset.add("orange")  # to Add Items --
# print(thisset)

# tropical = {"pineapple", "mango", "papaya"}
# add elements  from tropical into thisset:-
# thisset.update(tropical)
# print(thisset)

#add any iterable--
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

#remove Set Items-
# thisset.remove("banana")
# thisset.discard("banana")
# x = thisset.pop()
# thisset.clear()
# del thisset

# print(thisset)

# Loop Items --

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# Join sets--

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3 , "a"}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)  #multiple sets add(join)
# myset = set1 | set2 | set3 |set4  #multiple sets add(join)
# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)  #join tuple in a set
# print(z)

# set1.update(set2) #updated () method of sets

# set3 = set1.intersection(set2)
# set3 = set1 & set2  # intersection 2nd way

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)  #intersection 3rd way
# print(set1)

# set3 = set1.difference(set2)
# set3 = set1 - set2 # 2nd way for difference
# print(set3)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2)

# set3 = set1 ^ set2  #symmetric difference()
# print(set3)