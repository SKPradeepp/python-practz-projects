import random

score = 0

while True:

    secret = random.randint(1, 10)
    chances = 3

    print("\n====== Number Guessing Game ======")
    print("Guess the number between 1 and 10")
    print("You have 3 chances")

    while chances > 0:

        guess = int(input("Enter your guess: "))

        if guess == secret:
            print("Correct! You guessed the number.")
            score += 1
            break

        elif guess > secret:
            chances -= 1
            print("Too high!")

        else:
            chances -= 1
            print("Too low!")

        print("Chances left:", chances)

    else:
        print("Game Over!")
        print("The number was", secret)

    print("Score:", score)

    play = input("Play again? (yes/no): ")

    if play.lower() != "yes":
        print("Final Score:", score)
        print("Thanks for playing!")
        break