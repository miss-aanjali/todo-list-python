import random
secret_number = random.randint(1,10)
guess = None
print ("Welcome to the number guessing game!")
print("I have chosen a number between 1-10")
while guess != secret_number:
    guess = int(input("Choose a number"))
    if (guess < secret_number):
        print("This is too low!")
    elif(guess > secret_number):
        print("This is too high!")
    else:
        print("Congratulation! u have made the correct one")       