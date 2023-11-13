import random

while True:
    user_choice = input("Do you want to play the Number Guessing Game? "
                      "(yes/no): ").lower()

    if user_choice == "no":
        print("Thank you for playing! Goodbye.")
        break

    # Greet the player and explain the rules
    print("Welcome to the Number Guessing Game!")
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! I'm thinking of a number "
          f"between 1 and 100. Can you guess it?")

    # core logic
    guess = int(input("Enter guess number"))
    secret_number = random.randint(1, 100)
    if guess == secret_number:
        print(f"Congratulations, {player_name}")
        break
    else:
        print("Wrong guess number!Better luck next time")









