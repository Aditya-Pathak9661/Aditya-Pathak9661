#A dictionary is a collection which is ordered*,
#  changeable and do not allow duplicates.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 ,
#   "year": 2020,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)
# print(thisdict["brand"])
# print(len(thisdict))

# x = thisdict["model"]
# x = thisdict.get("year")
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# thisdict["color"] = "red"  # adding Items
# thisdict.update({"color": "red"})
# thisdict.pop("model")  #remove items
# thisdict.popitem()
# del thisdict["model"] #delete/ remove
# thisdict.clear()  # clear data
# del thisdict # delete dictionary

# print(thisdict) 

# x = car.keys()  # get keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# x = car.values()  # Get values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# x = car.items()   # get items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values --
# thisdict["year"] = 2018
# thisdict.update({"year": 2020})

# Loop Dictionaries --
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:  #looping value
#   print(thisdict[x])
# for x in thisdict.values(): #value
#   print(x)

#   for x in thisdict.keys(): #keys 
#     print(x)

# for x, y in thisdict.items():  # x , y values , keys
#   print(x, y)

# mydict = thisdict.copy()  #copy 
# print(mydict)

# mydict = dict(thisdict)
# print(mydict)

# myfamily = {
#   "child1" : {
#     "name" : "aditya",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "rishu",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linux",
#     "year" : 2011
#   }
# }

# print(myfamily) # nested dict.

# 2nd way --
# child1 = {
#   "name" : "aditya",
#   "year" : 2004
# }
# child2 = {
#   "name" : "rishu",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linux",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)
# print(myfamily["child2"]["name"])  #access method

# access method by Loop --

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])
