import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Dice Rolling Simulator")

    while True:
        dice = roll_dice()
        print("You rolled:", dice)

        choice = input("Do you want to roll again? (yes/no): ").lower()

        if choice != "yes":
            print("Thanks for playing!")
            break

main()
