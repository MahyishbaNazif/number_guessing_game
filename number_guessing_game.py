import random

print("=" * 50)
print("🎮 NUMBER GUESSING GAME")
print("=" * 50)

while True:

    print("\nSelect Difficulty")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("\nThanks for playing!")
        break

    if choice == "1":
        lower = 1
        upper = 50

    elif choice == "2":
        lower = 1
        upper = 100

    elif choice == "3":
        lower = 1
        upper = 500

    else:
        print("Invalid choice.")
        continue

    secret = random.randint(lower, upper)
    attempts = 0

    print(f"\nGuess the number between {lower} and {upper}")

    while True:

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret:
                print("📉 Too Low!")

            elif guess > secret:
                print("📈 Too High!")

            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter numbers only.")

    again = input("\nPlay Again? (Y/N): ").lower()

    if again != "y":
        print("\nGoodbye!")
        break