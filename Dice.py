import random

def roll_dice():
    dice_total= random.randint(1, 6) + random.randint(1, 6)
    return dice_total
def main():
    player1 = input("please enter player-1 name: - \n")
    player2 = input("please enter player-2 name: - \n")
    roll1 = roll_dice()
    roll2 = roll_dice()
    print(f"{player1} dice outcome is {roll1}")
    print(f"{player2} dice outcome is {roll2}")
    if roll1>roll2:
        print(f"{player1} wins")
    elif roll2>roll1:
        print(f"{player2} wins")
    else:
        print("it is a tie")

main()




