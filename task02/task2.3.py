"""
Write a program that prints the numbers from 1 to 100, but for multiples
of three print “Fizz” instead of the number and
for multiples of five print “Buzz”.
For numbers which are multiples of both three and five, print “FizzBuzz”.
"""

fizzbuzz: int
for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
