import random
import time

# Function to generate a random OTP
def generate_otp(length=6):
    otp = ''.join(random.choices('0123456789', k=length))
    return otp

# Function to display instructions
def display_instructions():
    print("Welcome to the Dynamic OTP Guessing Game!")
    print("An OTP (One-Time Password) will be generated and sent to you.")
    print("You need to guess the OTP correctly within 3 attempts.")
    print("Each time you guess, you'll get a hint.")
    print("Let's get started!\n")

# Function to get user input and validate the guess
def get_user_guess():
    while True:
        user_input = input("Enter your guess for the OTP: ")
        if user_input.isdigit():
            return user_input
        else:
            print("Invalid input! Please enter a numeric OTP.")

# Function to check the user's guess against the generated OTP
def check_guess(otp, guess):
    if otp == guess:
        return True
    return False

# Function to give hints based on the guessed OTP
def give_hint(otp, guess):
    hints = []
    # Compare only up to the length of the shorter string (otp or guess)
    for i in range(len(otp)):
        if i < len(guess):
            if otp[i] == guess[i]:
                hints.append(otp[i])  # Correct guess
            else:
                hints.append('_')  # Incorrect guess
        else:
            hints.append('_')  # If the guess is shorter than OTP
    return ''.join(hints)

# Function to display the score based on correct attempts
def display_score(attempts_left, total_attempts):
    score = (attempts_left / total_attempts) * 100
    print(f"Your score is: {score:.2f}%")
    return score

# Function to prompt the user to play again
def play_again():
    response = input("Do you want to play again? (yes/no): ").strip().lower()
    return response == 'yes'

# Main function to run the OTP guessing game
def start_game():
    attempts = 3  # Allow the user 3 attempts
    total_attempts = attempts  # Total attempts for scoring
    play = True
    
    while play:
        display_instructions()
        otp = generate_otp()  # Generate OTP
        print(f"A new OTP has been generated. You have {attempts} attempts to guess it.\n")

        start_time = time.time()  # Start the timer
        while attempts > 0:
            guess = get_user_guess()
            
            if check_guess(otp, guess):
                print("Congratulations! You guessed the OTP correctly!")
                display_score(attempts, total_attempts)
                break
            else:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
                hint = give_hint(otp, guess)
                print(f"Hint: {hint}\n")
        
        # If the user runs out of attempts
        if attempts == 0:
            print(f"Sorry, you've used all attempts! The correct OTP was: {otp}")
            display_score(attempts, total_attempts)
        
        end_time = time.time()  # End the timer
        print(f"Game Over! Total time: {end_time - start_time:.2f} seconds")
        
        # Ask the user if they want to play again
        play = play_again()
        if play:
            attempts = total_attempts  # Reset attempts for the new game
            print("\nStarting a new game...\n")
        else:
            print("Thank you for playing the OTP Guessing Game. Goodbye!\n")
            break

# Entry point of the program
if __name__ == "__main__":
    start_game()




