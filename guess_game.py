import random

def play_game():
    """Run a number guessing game in the terminal."""
    print("=" * 40)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 40)

    while True:
        try:
            upper = int(input("\nChoose an upper limit (e.g. 100): "))
            if upper < 2:
                print("Please enter a number greater than 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    secret = random.randint(1, upper)
    attempts = 0
    max_attempts = max(5, upper.bit_length() + 2)  # smart cap based on range

    print(f"\nI've picked a number between 1 and {upper}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret:
            print(f"  Too low!  ({remaining - 1} attempts left)" if remaining > 1 else "  Too low!")
        elif guess > secret:
            print(f"  Too high! ({remaining - 1} attempts left)" if remaining > 1 else "  Too high!")
        else:
            print(f"\n🎉 Correct! The number was {secret}.")
            print(f"   You got it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            break
    else:
        print(f"\n💀 Game over! The number was {secret}. Better luck next time!")

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again == "y":
        play_game()
    else:
        print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
    play_game()
