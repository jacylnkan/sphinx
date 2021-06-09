"""Another module."""

from ..package1.module1 import add_two_numbers, multiply_two_numbers 

def multiply_then_add(a: int, b, c):
    """[summary]

    Args:
        a (int): [description]
        b ([type]): [description]
        c ([type]): [description]

    Returns:
        [type]: [description]
    """
    sum_val = add_two_numbers(a, b)
    result = multiply_two_numbers(sum_val, c)
    return result 


def new_function_v2():
    """Display string for version 2.

    Returns:
        str: Describes version.
    """
    return "This is version 2."