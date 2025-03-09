import random 

print("Guess number Between 1 to 50")
number = random.randint(1, 50)

while True:
    guess = int(input("Enter your guess number: "))
    if guess < number:
        print("Too Low Number!")
    elif guess > number:
        print("Too High Number!")
    else:
        print("You Guess the correct Number")
        break
