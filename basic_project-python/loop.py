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

#make a list of devops tools and print all one-by-one , using loop-
devops_course=['linux','scripting', 'networking ', 'aws', 'git & github', 'jenkins', 'gitlab', 'docker', 'terraform', 'kubernetes', 'ansible']
for i in devops_course:
    print(i, end=" , ")

