#there are three way --
# a.if Else --

# #check a is greater or not
a = int(input("enter any number: "))
if (a >= 10):
     print("a is greater than number")
else:
     print("a is less than number")

 #check num is odd or even
num = int(input("enter number: "))
if num% 2 == 0:
     print(f"{num} is even number")
else:
     print(f"{num} is odd number")

# b. else if -
# check weather brfore go outside
weather = str(input("enter weather before go out(sunny , cloud, other):"))
if weather == "sunny":
    print("play indoor games")
elif weather == "cloud":
    print("go to play")
else:
    print('not understand | stay at home')

#check number is grater and less or equal to a :-
a = int(input("enter any number: "))
if (a > 10):
    print("a is greater than number")
elif (a < 10):
    print("a is less than number")
else:
    print("a is equal to number")

# c. nested if -

#compare between x and y --
x = int (input("enter value of x:"))
y = int (input("enter value of y:"))
if x> 5:
    if y > 5: 
        print("both x and y is greater than 5")
    else:
        print("x is greater 5 but y is not")
elif y > 5:
    if x > y:
         print("both x and y is greater than 5")
    else:
        ("y is greater 5 but x is not")
else:
    print("both x and y is lesser than 5")