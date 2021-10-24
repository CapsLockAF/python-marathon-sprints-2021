# Write  the function day_of_week(day) whose input parameter is a number
# or string representation of number. The function returns
# the corresponding day of the week if the input parameter is in
# the range of 1 to 7, namely
#
# · in the case when the input parameter is 5 the function should be
# displayed the message – "Friday"
# · in the case when the input parameter is not in the range of 1 to 7
# the function should be displayed the message – "There is no such
# day of the week! Please try again."
# · in the case of incorrect data the function should be displayed
# the message - "You did not enter a number! Please try again."
#
# Note: in the function you must use the "try except" construct.

# Function example:
# day_of_week(2)            "Tuesday"
# day_of_week(11)    "There is no such day of the week! Please try again."
# day_of_week("Monday")   "You did not enter a number! Please try again."

def day_of_week(day):
    try:
        n = int(day)
        week = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        return 0 < n < 8 and f"{week[n - 1]}" or \
            "There is no such day of the week! Please try again."
    except (ValueError, TypeError):
        return "You did not enter a number! Please try again."
