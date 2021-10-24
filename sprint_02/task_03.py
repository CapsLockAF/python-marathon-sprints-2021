# The string defining the points of the quadrilateral has the next
# form: "#LB1:1#RB4:1#LT1:3#RT4:3"
#
#  LB - Left Bottom point
#  LT - Left Top point
#  RT - Right Top point
#  RB - Right Bottom point
# numbers after letters are the coordinates of a point.
# Write a function figure_perimetr() that calculates the perimeter of
# a quadrilateral
#
# The formula for calculating the distance between points:
# ------------------------
#
# For example:

# Test	Result
# test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# print(figure_perimetr(test1))
# 10.0
# test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
# print(figure_perimetr(test2))
# 18.73454147995595
import re
import math

def figure_perimetr(s):
    lst = [(int(i[0]), int(i[1])) for i in re.findall(r"(\d):(\d)", s)]
    res = (math.sqrt(pow( (lst[1][0] - lst[0][0]), 2 ) + pow( (lst[1][1] - lst[0][1]), 2 )))\
        + (math.sqrt(pow( (lst[3][0] - lst[2][0]), 2 ) + pow( (lst[3][1] - lst[2][1]), 2 )))\
        + (math.sqrt(pow( (lst[2][0] - lst[0][0]), 2 ) + pow( (lst[2][1] - lst[0][1]), 2 )))\
        + (math.sqrt(pow( (lst[3][0] - lst[1][0]), 2 ) + pow( (lst[3][1] - lst[1][1]), 2 )))

    return round(res)


