"""
Write a program that check whether a string is palindrome or Not.
"""
my_str = 'bIbohPhoBib'

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")

