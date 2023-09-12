class HangBoard:
    """
    Initializes with 4 parameters:
    player: String (player name input from main)
    word: String (random generated word from wordgen)
    current_word: String (updated word as user guesses, from hang_board)
    alphabet_choices: Dictionary (letters as key, and their replacement for guesses as values)
    """
    def __init__(self, player, word, current_word, alphabet_choices):
        self._player = player
        self._word = word
        self._current_word = current_word
        self._alphabet_choices = alphabet_choices
        self._board = None

    def get_player(self):
        """
        Get player name
        :return: String (player name)
        """
        return self._player

    def get_current_word(self):
        """
        Get the current state of the word
        :return: String (current_word with non-guessed letters as dashes)
        """
        return self._current_word

    def get_remaining_choices(self):
        """
        Get the remaining alphabet choices
        :return: String (made from dictionary in alphabet_data)
        """
        return self._remaining_choices

    def update_current_word(self, guess):
        """
        Take the current word, which begins as dashes, and update it as guesses are correct to replace the dash with
        the corresponding letter
        :param guess: String (single letter from remaining choices)
        :return: String (the current word after the guess goes through)
        """
        updated_word = ""
        for letter in self._word:
            if letter != guess and letter != " ":
                letter = "_"
            updated_word += letter

        self._current_word = updated_word

        return self._current_word


my_game = HangBoard("Joe", "chester chesterson", "____", "A")

my_game.update_current_word("t")

print(my_game.get_current_word())



