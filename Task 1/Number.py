import random
import math

def guessing_game():
    # User inputs the lower and upper bounds of the range
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random integer within the specified range
    random_number = random.randint(lower_bound, upper_bound)
    
    # Calculate the maximum number of guesses allowed using the formula
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    
    print(f"\nYou have {max_guesses} attempts to guess the number.\n")
    
    # Initialize the number of guesses
    guess_count = 0
    
    while guess_count < max_guesses:
        guess = int(input("Enter your guess: "))
        guess_count += 1
        
        if guess > random_number:
            print("Try Again! You guessed too high.")
        elif guess < random_number:
            print("Try Again! You guessed too small.")
        else:
            print(f"Congratulations! You guessed the number in {guess_count} attempts.")
            return
    
    print("Better Luck Next Time! You've exhausted all your guesses.")
    print(f"The correct number was: {random_number}")

# Run the game
guessing_game()
