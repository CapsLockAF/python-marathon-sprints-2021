# Create function create_account(user_name: string, password: string,
# secret_words: list). This function should return inner function check.
#
# The function check compares the values of its arguments with password and
#     secret_words: the password must match completely, secret_words
#     may be misspelled (just one element).
#
# Password should contain at least 6 symbols including one uppercase letter,
#     one lowercase letter,  special character and one number.
#
# Otherwise function create_account raises ValueError.
#
# For example:
#
# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error
#
# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])
#
# then
#
# tom("Qwerty1_",  ["1", "word"]) return True
#
# tom("Qwerty1_",  ["word"]) return False due to different length of
# ["1", "word"] and  ["word"]
#
# tom("Qwerty1_",  ["word", "12"]) return True
#
# tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!"
# not equals to "Qwerty1_"
import re


def create_account(user_name, password, secret_words):
    ptrn = re.compile(r'^.*(?=.{,})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)(?=.*[!@£$%^&*()_+={}?:~\[\]])[a-zA-Z0-9!@£$%^&*()_+={}?:~\[\]]+$')

    def check(p, w):
        if p == password and len(secret_words) != len(w) + 1:
            arr = []
            for x in w:
                for y in secret_words:
                    if x == y \
                        or x[:len(x) - 1] == y \
                        or x[1:] == y \
                        or x == y[:len(y) - 1] \
                        or x == y[1:]:
                            if x not in arr:
                                arr.append(x)
            return len(arr) + 1 == len(w) and len(w) - 1 == len(secret_words) or len(arr) == len(w) and True
        else:
            return False

    if re.fullmatch(ptrn, password) and len(secret_words):
        return check
    else:
        raise ValueError

