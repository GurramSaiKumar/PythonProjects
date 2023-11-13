import random

while True:
    quit_game = input("Do you want to play the Number Guessing Game? (yes/no): ").lower()

    if quit_game != "yes":
        print("Thank you for playing! Goodbye.")
        break

    secret_number = random.randint(1, 100)
    attempts = 0

    # Greet the player and explain the rules
    print("Welcome to the Number Guessing Game!")
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! I'm thinking of a number between 1 and 100. Can you guess it?")

    guess = input("Enter your guess: ")
    guess = int(guess)
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations, {player_name}! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number")


