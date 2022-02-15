"""
Taylor series
"""
from itertools import count
from typing import Union
import math

EPSILON = 0.0001



def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    sum_ = 1
    for n in count(1, 1):
        current_item = x ** n / math.factorial(n)
        sum_ += current_item
        if current_item <= EPSILON:
            break

    # print(x)
    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    return 0
