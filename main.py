def main():
    player_name = input("Hello. My name is Chester, the Hangman Guru. Isn't Hangman the best? So much strategy, "
                        "so many delightful choices. Oh, I'm sorry. Where are my manners. What is your name? \n")

    print \
        ("\nNice to meet you, " + player_name + ". I would love to a play a game of Hangman. But I will let you choose "
                                                "the difficulty.")

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

        return check_choice

    choose_difficulty()


main()
