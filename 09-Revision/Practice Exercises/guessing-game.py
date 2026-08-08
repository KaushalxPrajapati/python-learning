import random

def play_game():
    try:
        lucky_num = random.randint(1, 50)
        while True:
            guess = int(input("Guess a number: "))
            if guess == lucky_num:
                print("You Won. Game Over!")
                break
            elif guess < lucky_num:
                print("Guessed too LOW")
            else:
                print("Guessed too HIGH")

    except ValueError:
        print("Not a number")


play_game()
print("Thank you for playing...")
