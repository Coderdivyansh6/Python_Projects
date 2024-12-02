import random

# Function for checking users guess and giving feedback
def check_guess(guess, num):
    if guess < num:
        return f"Your guess is too Small! Try guessing a number higher."
    elif guess > num:
        return f"Your guess is too Bigger! Try guessing a number lower."
    else:
        return "Correct!"

# Function to play the game
def play_game():
    print("Welcome to the Number Guessing Game!")
    
    # Asking user to choose difficuilty level
    difficulty = input("Choose your difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        number_range = 50
    elif difficulty == "medium":
        number_range = 100
    else:
        number_range = 200

    # Generating a range between 1 to the difficuilty level range
    guess = random.randint(1, number_range)
    attempts = 8

    print(f"Guess a number between 1 and {number_range}. You have {attempts} attempts.")
    
    count = 0
    while count < attempts:
        # Input validation
        while True:
            try:
                num = int(input(f"Attempt {count + 1}/{attempts} - Enter your guess: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Please enter a valid number.")

        # Check the guess and give feedback
        feedback = check_guess(num, guess)
        print(feedback)
        
        if feedback == "Correct!":
            print(f"You won the game! {attempts - count - 1} attempts remaining.")
            break
        
        count += 1
        print(f"Attempts remaining: {attempts - count}")

    if count >= attempts and guess != num:
        print(f"Game over! The correct number was {guess}.")

# Main function to start the game and handle replay
def main():
    play_again = "yes"
    while play_again.lower() == "yes":
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")

if __name__ == "__main__":
    main()
