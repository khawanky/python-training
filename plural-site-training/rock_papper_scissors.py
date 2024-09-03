import random

comp_choice = random.choice(['rock','paper','scissors'])
user_choice = input('Do you want rock, paper, or scissors?\n')

result = ""

if comp_choice == user_choice:
    result="TIE,"
elif (user_choice=="rock" and comp_choice=="scissors") or (user_choice=="paper" and comp_choice=="rock") or (user_choice=="scissors" and comp_choice=="paper"):
    result="You Win!"
else:
    result="You lose!"

print(f"{result} Computer choice was ", comp_choice, sep='')
