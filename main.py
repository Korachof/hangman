import hang_board
import wordgen
import alphabet_data
import play_hangman
import reset_game


def main():
    player_name = input("Hello. My name is Chester, the Hangman Guru. Isn't Hangman the best? So much strategy, "
                        "so many delightful choices. Oh, I'm sorry. Where are my manners. What is your name? \n")

    print("\nNice to meet you, " + player_name + ". I would love to a play a game of Hangman. But I will let you choose"
                                                 " the difficulty.")

    def choose_difficulty():
        """
        Where the user selects which difficult of Hangman they want. Will recur until user selects their preferred
        and available option.
        :return: String (the choice, which is a number that is a string)
        """
        difficulty = None

        while difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4":
            difficulty = input(
                "Please choose a difficulty by typing the number corresponded to that difficulty setting "
                "and pressing Enter\n"
                "1) Easy - 5 letters or fewer \n"
                "2) Medium - 8 letters or fewer \n"
                "3) Hard - 11 letters or fewer \n"
                "4) Insane - Over 11 letters \n")

        check_choice = input("You selected " + difficulty + " . Is this correct? \n"
                                                            "Type Y for yes and N for No \n")

        if check_choice.upper() != "Y":
            choose_difficulty()

        return difficulty

    difficulty = choose_difficulty()

    generated_word = wordgen.get_game_word(difficulty)

    our_game = hang_board.HangBoard(player_name, generated_word, wordgen.create_hidden_word(generated_word),
                                    alphabet_data.alphabet, " ")

    print("Great! Now that my trusty machine has found a word for us, let's begin! You can go first. I've provided "
          "your options below")

    play = play_hangman.play_game(our_game)

    if play is True:
        print("Incredible! You win! \n")
        print("The word was " + our_game.get_word() + "\n")
        play = reset_game.reset()

    # if user wants to retry, reset
    if play == "Y":
        main()


main()

