import random

def number_guessing_game():
    secret_num = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    attempt = 0

    while True:
        attempt += 1
        guess = int(input("Take a guess: "))

        if guess == secret_num:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
        elif guess < secret_num:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

number_guessing_game()