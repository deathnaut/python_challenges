"""
Write a program that will output the N-th term of the Fibonacci sequence.
For example: print fib(6) should output 8.
"""

input = int(input("(fibonacci sequence) enter an integer: "))

def fib(n):
    x = 0
    y = 1
    for i in range(0, n):
        num = x
        x = y
        y = num + y
    print(x)

fib(input)
