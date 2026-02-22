import random
secret_number = random.randint(1, 100)
max_attempts = 5
attempts = 0
print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts. Good luck!\n")
while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == secret_number:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")
        print(f"Attempts left: {max_attempts - attempts}\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")
if attempts == max_attempts and guess != secret_number:
    print(f"💀 Game Over! The correct number was {secret_number}.")
