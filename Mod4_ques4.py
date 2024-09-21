import random
def guessing_game():
    number_to_guess = random.randint(1, 10)
    while True:
        # User input
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
            if user_guess < number_to_guess:
                print("Too low")
            elif user_guess > number_to_guess:
                print("Too high")
            else:
                print("Correct! You guessed the right number.")
                break

        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")
              guessing_game()
