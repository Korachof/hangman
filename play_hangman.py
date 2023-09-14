import hang_board

def play_game(hangman_class):
    print(hangman_class.get_remaining_choices())
    print("\n \n")
    print(hangman_class.get_hangman_pic())
    print("\n \n")
    print(hangman_class.get_current_word())
    guess = input("Please type the letter you would like to guess from the remaining options and press Enter \n")
    update_alpha = hangman_class.update_alphabet_options(guess)

    # if the guess is not in the remaining options then start over and guess again
    if update_alpha is False:
        play_game(hangman_class)

    guess_bool = hangman_class.update_current_word(guess)

    # Guess is incorrect
    if guess_bool is False:
        print("Oh I'm sorry. That guess is incorrect. \n")

        update = hangman_class.update_hangman_pic()

        if update is not None and update.upper() == "Y":
            return update.upper()

        play_game(hangman_class)

    # Guess is correct
    elif guess_bool is True:
        print("Awesome! You guessed correctly! \n")

        if hangman_class.get_current_word() != hangman_class.get_word():
            play_game(hangman_class)

        print("Incredible! You win! \n")



