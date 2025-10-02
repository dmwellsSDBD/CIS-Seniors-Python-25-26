import random

# =============================================================================
# LUCKY NUMBER GUESSING GAME
# This program demonstrates while loops, break statements, and random numbers
# =============================================================================

# Game statistics variables - track performance across all rounds
total_rounds = 0      # Count how many rounds have been played
total_wins = 0        # Count how many rounds were won
total_guesses = 0     # Sum of all guesses made across all rounds

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - allows playing multiple rounds
# This is a while True loop that continues until player chooses to quit
while True:
    # Generate a random lucky number between 1 and 50 (inclusive)
    lucky_number = random.randint(1, 50)
    
    # Set the maximum number of attempts allowed per round
    max_attempts = 7
    
    # Initialize the attempt counter for this round
    attempts = 0
    
    # Display round information
    print(f"\n{'='*50}")
    print(f"  ROUND {total_rounds + 1}")
    print(f"{'='*50}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {max_attempts} attempts to guess it!")
    print()
    
    # Guessing loop - this is a count-controlled while loop
    # It continues as long as the player has attempts remaining
    while attempts < max_attempts:
        # Get user's guess with error handling
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("X Please enter a valid number!")
            continue
        
        # Increment the attempt counter
        attempts += 1
        
        # Check if the guess is correct
        if guess == lucky_number:
            # Player wins this round!
            print()
            print("*" * 25)
            print(f"  CONGRATULATIONS! You guessed the lucky number {lucky_number}!")
            print(f"  It took you {attempts} attempt(s)!")
            print("*" * 25)
            
            # Update game statistics
            total_wins += 1
            total_guesses += attempts
            
            # Break out of the guessing loop since player won
            break
            
        # Provide hints to help the player
        elif guess < lucky_number:
            print(f"Too low! The lucky number is higher than {guess}.")
        else:  # guess > lucky_number
            print(f"Too high! The lucky number is lower than {guess}.")
    
    else:
        # This else clause executes only if the while loop completes naturally
        # (without hitting a break statement), meaning player ran out of attempts
        print()
        print("X" * 25)
        print(f"  GAME OVER! You've used all {max_attempts} attempts!")
        print(f"  The lucky number was {lucky_number}.")
        print("X" * 25)
        
        # Still count the guesses even though player lost
        total_guesses += attempts
    
    # Increment the round counter
    total_rounds += 1
    
    # Display statistics for this round
    print()
    print("-" * 50)
    print(f"Round {total_rounds} Statistics:")
    print(f"  • Lucky Number: {lucky_number}")
    print(f"  • Attempts Used: {attempts}/{max_attempts}")
    print(f"  • Result: {'WIN ✓' if attempts <= max_attempts and guess == lucky_number else 'LOSS ✗'}")
    print("-" * 50)
    
    # Ask if player wants to play another round
    # This while True loop with break provides input validation
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
        
        if play_again in ['yes', 'y']:
            # Continue to next iteration of main game loop
            break
        elif play_again in ['no', 'n']:
            # Break out of main game loop to end the program
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    # If player chose not to play again, break out of main game loop
    if play_again in ['no', 'n']:
        break

# Display final game statistics
print()
print("=" * 50)
print("  FINAL GAME STATISTICS")
print("=" * 50)
print(f"Total Rounds Played: {total_rounds}")
print(f"Rounds Won: {total_wins}")
print(f"Win Rate: {(total_wins/total_rounds*100) if total_rounds > 0 else 0:.1f}%")
print(f"Total Guesses Made: {total_guesses}")

if total_wins > 0:
    print(f"Average Guesses per Win: {total_guesses/total_wins:.1f}")

print("=" * 50)
print("\n Thanks for playing the Lucky Number Guessing Game!")
print("Goodbye!")