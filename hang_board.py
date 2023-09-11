class HangBoard:
    def __init__(self, player, word, current_word, alphabet_choices):
        self._player = player
        self._word = word
        self._current_word = current_word
        self._alphabet_choices = alphabet_choices
        self._board = None

    def get_player(self):
        return self._player

    def get_current_word(self):
        return self._current_word

    def get_remaining_choices(self):
        return self._remaining_choices

    def update_current_word(self, guess):
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



