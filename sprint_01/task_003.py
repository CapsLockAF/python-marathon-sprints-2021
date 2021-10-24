# Given a string, check if its characters can be rearranged to form
# a palindrome. Where a palindrome is a string that reads
# the same left-to-right and right-to-left.
#
# Example
#
# "trueistrue" -> false;
# "abcab" -> true because "abcba" is a palindrome
# [input] string s (min 1 letters)
#
# [output] boolean

def isPalindrome(str):
    letters_list = [(str.count(lttr), lttr) for lttr in str]
    fltr = set(filter(lambda x: x[0] % 2 != 0, letters_list))

    return True if len(fltr) < 2 else False
