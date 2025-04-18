#problem statement--
'''
*
**
***
****
'''
row = 1
while row <= 4:
    col=1
    while col <= row:
        print(" *", end="")
        col = col+1
    print()
    row = row+1

'''
***
***
***
'''
for i in range(4):
    print("\t ****")

#table --
for i in range(1, 11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j} ", end="\t")
    print(" ")