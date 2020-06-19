def guess_game():
    secret_word = "Donkey"
    guess = ""
    guess_count = 0
    guess_limit = 5
    guess_response = {
        "Chicken": "No, it's not a bird.",
        "Horse": "You're close, it looks like a horse.",
        "Goat": "Nah. Not a goat.",
        "Pig": "Nope. Not a pig.",
        "Sheep": "Sheep are so cute. But no, it's not a sheep.",
        "Cow": "No, not a cow.",
        "Rabbit": "I love rabbits. But no, it's not a rabbit.",
        "Duck": "No, it's not a bird.",
    }
    print()
    print("Welcome to the Guessing Game! To win, enter the secret word (hint: think farm animal)")
    print()

    while True:
        if guess_count == (guess_limit - 1):
            print("You have one guess left...", '\n')
        guess = input("Enter guess: ").title()
        if guess != secret_word:
            print(guess_response.get(guess, "Incorrect secret word, try again."), '\n')
        else:
            print("Correct! You win!")
            return True
        guess_count = guess_count + 1
        if guess_count >= guess_limit:
            print("Invalid secret word. You lose.")
            return False

while True:
    if not guess_game():
        play_again = input("Want to play again (y/n)?: ").lower()
        if play_again == 'n':
            print("Goodbye!")
            break
    else:
        break

