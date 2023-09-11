from random_word import RandomWords
from better_profanity import profanity


def get_game_word(difficulty):
    """
    Use the random-word package to find a random English word for the hangman game.
    Utilizes the better_profanity package to check if the word is appropriate for all ages
    :param difficulty: INT (Easy: 1, Medium: 2, Hard: 3, Insane: 4)
    :return: String (the word)
    """
    game_word = None

    if difficulty == 1:
        while game_word is None or profanity.contains_profanity(game_word) is True or len(game_word) > 5:
            game_word = RandomWords().get_random_word()

    elif difficulty == 2:
        while game_word is None or profanity.contains_profanity(game_word) is True \
                or 5 > len(game_word) or len(game_word) > 8:
            game_word = RandomWords().get_random_word()

    elif difficulty == 3:
        while game_word is None or profanity.contains_profanity(game_word) is True \
                or 8 > len(game_word) or len(game_word) > 11:
            game_word = RandomWords().get_random_word()

    elif difficulty == 4:
        while game_word is None or profanity.contains_profanity(game_word) is True or len(game_word) < 11:
            game_word = RandomWords().get_random_word()

    return game_word






