def get_digit(number, position):
    """
    get digit at a particular position
    >>> get_digit(123,0)
    3
    >>> get_digit(123,2)
    1
    """
    return number // (10 ** position) % 10
