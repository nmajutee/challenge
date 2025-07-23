import random

secret_number = random.randint(1, 10)
guess_count = 0
while True:
    guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
    guess_count += 1

    match guess:
        case _ if guess == secret_number:
            print(f"Congratulations, you guessed it! The number was {secret_number}. After {guess_count} attempts.")
        case _ if guess < secret_number:
            print(f"Too low! Try again. You've made {guess_count} attempts.")
        case _ if guess > secret_number:
            print(f"Too high! Try again. You've made {guess_count} attempts.")
        case _:
            print("Invalid input. Please enter a number between 1 and 10.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

