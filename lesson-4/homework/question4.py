import random

while True:
    number_guess = random.randint(1, 100)
    count = 10

    while count > 0:
        try:
            user_guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < number_guess:
            print("Too low!")
        elif user_guess > number_guess:
            print("Too high!")
        else:
            print("You guessed it right!")
            break

        count -= 1

    if count == 0:
        print("You lost. Want to play again? ")

    else:
        print("Want to play again?")

    user_try_again = input().lower().strip()
    if user_try_again not in ['y', 'yes', 'ok']:
        print("Thanks for playing!")
        break
