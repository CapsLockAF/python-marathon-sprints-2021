# As input data, you have a list of strings.
#
# Write a method double_string() for counting the number of strings from
# the list, represented in the form of the concatenation of two strings
# from this arguments  list
#
# For example:
#
# Test	Result
# data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
# print(double_string(data))
# 3
# data = ['aa', 'abc', 'qwerqwer']
# print(double_string(data))
# 0

import re


def double_string(d):
    c = []
    s_tmp = f" {' '.join(d)} "
    for s in d:

        pattern = r"\s(" + s + s + r")\s"
        if s*2 not in c:
            c += re.findall(pattern, s_tmp)
        else:
            for j in d:
                if (s + j) in d and (s + j) not in c:
                    c.append(s + j)
                elif (j + s) in d and (j + s) not in c:
                    c.append(j + s)
    return c

