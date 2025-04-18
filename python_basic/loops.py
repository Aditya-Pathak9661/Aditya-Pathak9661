# in python we study for loop and while loop --
#a. while loops-
n = 5
i = 1
while i<n:
    print(i)
    i+=1

# contral statement-
# after while is succesfully run then else statement run
n = 10
i = 1
while i<=n:
    print(i*2)
    i+= 1
else:
    print("👆this is a table of 2")

# break statement- stop the loop after using it
n= int(input("enter value: "))
i= 0
while i < n:
    i = i+1 # i+=1
    if i == 5:
        break
    print(i)
else: # this else will also not run , due to break statement
    print("break statement is run in loop")

#continue - skip the iteration
n= int(input("enter value: "))
a= int(input("enter value: "))
i= 0
while i < n:
    i = i+1 # i+=1
    if i == a:
        continue
    print(i)
else: # this else will also not run , due to break statement
    print("continue statement is run in loop")


# for loop--
for i in "aditya":
    print(i)

list1 = ["apple", "banana" , "orange", "grapes", "mango"]
for i in list1:
    if i == 'orange':
        break
    print(i)

list2 = ["apple", "banana" , "orange", "mango", "lichi"]
for i in list2:
    if i == 'banana':
        continue
    print(i)

list4= list(range(0,6)) #last one is not include in range
print(list4)

#range(start, stop, step)
#table of 2-
for i in range(2, 21, 2):
    print(i , end=" ")