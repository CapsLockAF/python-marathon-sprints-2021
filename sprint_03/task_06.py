# Generator function randomWord has as an argument list of words.
# It should return any random word from this list. Each time words are
# different until the end of the list is reached. Then words are taken
# from the initial list again.
#
# For example if
# list = ['book', 'apple', 'word']
#
# books = randomWord(list)
# then possible output example
# first call of next(books) returns apple
# second call of next(books) returns book
# third call of next(books) returns word
# fourth call of next(books) returns book

import random

def randomWord(lst):
    if not lst:
        yield None
    lst_copy = list(lst)
    random.shuffle(lst_copy)
    lst_set = []
    i = 0
    while i <= len(lst_copy):
        if i == len(lst_copy):
            i -= random.randint(1, len(lst_copy))
            yield lst_copy[i]
        elif lst_copy[i] in lst_set:
            yield lst_copy[i]
        else:
            lst_set.append(lst_copy[i])
            yield lst_copy[i]
        i += 1
