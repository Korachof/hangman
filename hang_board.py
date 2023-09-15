import hangmanpics
import reset_game


class HangBoard:
    """
    Initializes with 4 parameters:
    player: String (player name input from main)
    word: String (random generated word from wordgen)
    current_word: String (updated word as user guesses, from hang_board)
    alphabet_choices: Dictionary (letters as key, and their replacement for guesses as values)
    """
    def __init__(self, player, word, current_word, alphabet_choices, hangman_pic):
        self._player = player
        self._word = word
        self._current_word = current_word
        self._alphabet_choices = alphabet_choices
        self._hangman_pic = hangman_pic
        self._hangman_level = 0
        self._board = None
        self._correct_guesses_dict = {}

    def get_player(self):
        """
        Get player name
        :return: String (player name)
        """
        return self._player

    def get_word(self):
        """
        Get the original word generated
        :return: String (original word)
        """
        return self._word

    def get_current_word(self):
        """
        Get the current state of the word
        :return: String (current_word with non-guessed letters as dashes)
        """
        return self._current_word

    def get_alphabet(self):
        """
        Get the list of alphabet options remaining
        :return: List
        """
        return self._alphabet_choices

    def get_remaining_choices(self):
        """
        Get the remaining alphabet choices
        :return: String (made from dictionary in alphabet_data)
        """
        display_choices = ""
        for element in self._alphabet_choices:
            display_choices += (element + " ")

        return display_choices

    def get_hangman_pic(self):
        """
        Gets the current hangman pic to show progress
        :return: String (ascii hangman pic)
        """
        return self._hangman_pic

    def get_hangman_level(self):
        """
        Gets the level the player is currently on (how close they are to dying)
        :return: the current level
        """
        return self._hangman_level

    def update_current_word(self, guess):
        """
        Take the current word, which begins as dashes, and update it as guesses are correct to replace the dash with
        the corresponding letter
        :param guess: String (single letter from remaining choices)
        :return: String (the current word after the guess goes through)
        """
        updated_word = ""
        for letter in self._word:
            if letter not in self._correct_guesses_dict and letter != guess and letter != " " and letter != "-":
                letter = "_"

            elif letter == guess:
                self._correct_guesses_dict[guess] = None

            updated_word += letter

        # if the word didn't change, then return False for incorrect guess
        if self._current_word == updated_word:
            return False

        self._current_word = updated_word

        return True

    def update_alphabet_options(self, guess):
        """
        Updates the alphabet options the player still has to guess
        :param guess: String (letter the user is guessing)
        :return: Bool (True if guess is in list, False otherwise)
        """
        for index in range(len(self._alphabet_choices)):
            if self._alphabet_choices[index] == guess:
                self._alphabet_choices.remove(guess)
                return True

        return False

    def update_hangman_pic(self):
        self._hangman_level += 1

        if self._hangman_level == 1:
            self._hangman_pic = hangmanpics.hangman_pic_levels[0]

        elif self._hangman_level == 2:
            self._hangman_pic = hangmanpics.hangman_pic_levels[1]

        elif self._hangman_level == 3:
            self._hangman_pic = hangmanpics.hangman_pic_levels[2]

        elif self._hangman_level == 4:
            self._hangman_pic = hangmanpics.hangman_pic_levels[3]

        elif self._hangman_level == 5:
            self._hangman_pic = hangmanpics.hangman_pic_levels[4]

        elif self._hangman_level == 6:
            self._hangman_pic = hangmanpics.hangman_pic_levels[5]

        elif self._hangman_level == 7:
            self._hangman_pic = hangmanpics.hangman_pic_levels[6]

            return False


