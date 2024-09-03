import random

player1=input('Enter player 1\n')
player2=input('Enter player 2\n')

def rool_dice():
    return random.randint(1,6) + random.randint(1,6)

roll1 = rool_dice()
roll2 = rool_dice()

print(f"Player {player1} rolled {roll1}")
print(f"Player {player2} rolled {roll2}")

