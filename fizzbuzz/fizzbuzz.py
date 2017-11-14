"""
For numbers 1 through 100, print fizz if the number is divisible by 3, buzz if
the number is divisible by 5 and fizzbuzz if the number if the number is divisible
by both 3 and 5. If the number isn't divisible by 3 or 5, just output the number itself.

The output should look something like 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz Buzz 16 17 Fizz...

"""

def fizzbuzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

fizzbuzz(100)
