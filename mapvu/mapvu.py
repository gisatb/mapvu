"""Main module."""

import string
import random

def generate_random_string(length=10, upper=False, digits=False, punctuation=False ):
    """Generate a random string of given length

    Args:
        length (int, optional): The length of the string to generate. Defaults to 10.
        upper (bool, optional): Whether to include uppercase letters. Defaults to False.
        digits (bool, optional): Whether to include lowercase letters. Defaults to False.
        punctuation (bool, optional): Whether to include pounctuation. Defaults to False.

    Returns:
        _type_: The generated string
    """    
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    if digits:
        letters += string.digits
    if punctuation:
        letters += string.punctuation 
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str 


def generate_lucky_number(length=1):
    """Generate a random number of given length

    Args:
        length (int, optional): The length of the number to generate. Defaults to 1.

    Returns:
        _type_: the generated numbers
    """    
    result_str = '' .join(random.choice(string.digits) for i in range(length))
    return int(result_str)
