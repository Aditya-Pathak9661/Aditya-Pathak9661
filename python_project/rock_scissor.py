'''
we love this game in childhood/school-time
this a game of rock, paper, scissor
'''
import random
game_items = ["rock", "paper", "scissor"]
user = input("enter your name: ")
choose_items = input("enter random items = rock, paper,scissor: ")
mach_choose = random.choice(game_items) #machine can choose it random

print(f"user choice ={choose_items}, computer choice= {mach_choose}")

if choose_items == mach_choose:
    print("match tie")
elif choose_items =="rock":
    if mach_choose == "paper":
        print("computer win!")
    else:
        print(f"{user} win")

elif choose_items == "paper":
    if mach_choose == "scissor":
        print("computer win!")
    else:
        print(f"{user} win")

elif choose_items == "scissor":
    if mach_choose == "paper":
        print("computer win!")
    else:
        print(f"{user} win")