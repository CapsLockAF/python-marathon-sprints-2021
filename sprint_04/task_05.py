# The basic premise of the game Gallows is to follow two rules:
#
# First character of next word must match last character of previous word.
# The word must not have already been said.
# Below is an example of a Gallows game:
#
# ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!
#
# ['motive', 'beach']  # invalid! - beach should start with "e"
#
# ['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
# Write a Gallows class that has two instance variables:
#
# words: a list of words already said.
# game_over: a boolean that is true if the game is over.
# and two instance methods:
#
# play: a method that takes in a word as an argument and checks if it
# is valid (the word should follow rules #1 and #2 above).
#
# If it is valid, it adds the word to the words list, and returns
# the words list.
# If it is invalid (either rule is broken), it returns "game over" and
# sets the game_over boolean to true.
# restart: a method that sets the words list to an empty one [] and
# sets the game_over boolean to false. It should return "game restarted".


# Examples:
# my_gallows = Gallows()
# my_gallows.play('apple') ➞ ['apple']
# my_gallows.play('ear') ➞ ['apple', 'ear']
# my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# my_gallows.words ➞ ['apple', 'ear', 'rhino']
# # Words should be accessible.
# my_gallows.restart() ➞ "game restarted"
# # Words list should be set back to empty.
# my_gallows.play('hostess') ➞ ['hostess']
# my_gallows.play('stash') ➞ ['hostess', 'stash']
# my_gallows.play('hostess') ➞ "game over"
# # Words cannot have already been said.
# my_gallows.play('apple') ➞ ['apple']
# my_gallows.play('ear') ➞ ['apple', 'ear']
# my_gallows.play('rhino') ➞ ['apple', 'ear', 'rhino']
# # Corn does not start with an "o".
# my_gallows.play('corn') ➞"game over"
# my_gallows.words ➞ ['apple', 'ear', 'rhino']
# my_gallows.restart() ➞ "game restarted"
# my_gallows.words ➞ []

class Gallows:
    def __init__(self):
        self.__game_over = False
        self.__words = []

    @property
    def words(self):
        return self.__words

    @property
    def game_over(self):
        return "game over" and self.__game_over

    def play(self, w):
        w_lst = self.__words

        if w in w_lst or w_lst and w_lst[-1][-1] != w[0]:
            self.__game_over = True
            return "game over"

        w_lst.append(w)
        return w_lst

    def restart(self):
        self.__words = []
        self.__game_over = False
        return "game restarted"
