# Write the function valid_email(...) to check if the input string is
# a valid email address or not.
#
# An email is a string (a subset of ASCII characters) separated into
# two parts by @ symbol, a “user_info” and a domain_info, that is
# personal_info@domain_info:
# in case of correct email the function should be displayed
# the corresponding message – "Email is valid"
# in case of incorrect email the function should be displayed t
# he corresponding message – "Email is not valid"
#
# Note: in the function you must use the "try except" construct.
#
# Function example:
#
# valid_email("trafik@ukr.tel.com")          #output:   "Email is valid"
#
# valid_email("trafik@ukr_tel.com")        #output:   "Email is not valid"
#
# valid_email("tra@fik@ukr.com")           #output:   "Email is not valid"
#
# valid_email("ownsite@our.c0m")         #output:   "Email is not valid"
import re


def valid_email(s):
    try:
        m = re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", s)
        return m and "Email is valid" or "Email is not valid"
    except TypeError:
        pass

