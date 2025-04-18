# operators -
# 1. arithmetic operators-

num1 = 122
num2 = 11

print(num1 + num2) #addition
print(type(num1 + num2)) 

print(num1 - num2) #subtract
print(num1 * num2) #multiplication
print(num1 // num2) #division
print(num1 % num2) #reminder
print(num1**2) 

#comparison operators -
a = 12 *3 -15 +32
b = 14 *4 -30 +41
c = 16 *3 -23 +18

print( a == c)
print( a == b)
print( a != c)
print( a <= b)
print( a >= c)
print( b == c)
print( b != c)

# logical -
print( a == c and b == a)
print( a <= c and b >= a)
print( a != c and b >= a)
print( a == c or b != a)

#bitwise -
x = 2
y = 5
z = 3

print(x & y) # and
print(x | z) # or
print(x << z) # right shift
print(x << y) # left shift

# assignment -
p = 12 # assig 12 as p
p+= 12 # p =24
print (p)
p-= 22 # p=2
print (p)
p*= 3 #p= 6
print (p)
p/= 3 #p=2
print (p)

#membership -
a = [12, 16, 24]

a1 = 12 in a
print(a1)

a2 = 16 not in a
print(a2)

#identity
n = 12
m = 14
print(n is m)
print(n is not m)