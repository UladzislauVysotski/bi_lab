"""
Write a program that check whether a string is palindrome or Not.
"""
from typing import Any, Iterator

my_str: str = 'bIbohPhoBib'

my_str = my_str.casefold()

rev_str: Iterator[Any] = reversed(my_str)

if not list(my_str) != list(rev_str):
    print("It is palindrome")
else:
    print('It is not palindrome')
