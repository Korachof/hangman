import hang_board



def play_game(hangman_class):
    """
    Function that allows the user to play through a game of hangman
    :param hangman_class: Class Object (hang_board.HangBoard)
    :return: Bool (True if the user completed the word, False if they lost)
    """
    print(hangman_class.get_remaining_choices())
    print(hangman_class.get_hangman_pic())
    print(hangman_class.get_current_word())
    guess = input("\nPlease type the letter you would like to guess from the remaining options and press Enter \n")
    update_alpha = hangman_class.update_alphabet_options(guess.lower())

    # if the guess is not in the remaining options then start over and guess again
    if update_alpha is False:
        keep_playing(hangman_class)

    guess_bool = hangman_class.update_current_word(guess.lower())

    # Guess is incorrect
    if guess_bool is False:
        print("Oh I'm sorry. That guess is incorrect. \n")

        update = hangman_class.update_hangman_pic()

        if update is False:
            return update

        keep_playing(hangman_class)

        if hangman_class.get_current_word() == hangman_class.get_word():
            return True

    # Guess is correct
    elif guess_bool is True:
        print("Awesome! You guessed correctly! \n")

        if hangman_class.get_current_word() != hangman_class.get_word():
            keep_playing(hangman_class)

        if hangman_class.get_current_word() == hangman_class.get_word():
            return True


def keep_playing(hangman_class):
    """
    A helper function to play_game() to prevent unintended recursive behavior
    :param hangman_class: Class Object (hang_board.HangBoard)
    :return: Function (play_game)
    """
    return play_game(hangman_class)

