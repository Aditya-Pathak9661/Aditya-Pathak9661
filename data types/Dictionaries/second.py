# print ("hello,world!")
# age = str(input("enter your age"))
# name = str(input("enter your name"))
# print(f"my name is {name}, {age} years old")


age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("you are not an adult")

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

age = 20
if age >= 18:
    if age >= 21:
        print("You can drink alcohol.")
    else:
        print("You cannot drink alcohol yet.")
else:
    print("You are not an adult.")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

    
i = 0
while i < 5:
    print(i)
    i += 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()