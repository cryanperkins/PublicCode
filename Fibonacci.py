__author__ = 'Ryan Perkins'


def intro():
    number = input("Choose a number  to find out the Fibonacci sequence up to that number.")
    return fib(number)


def fib(n):
    a, b = 0, 1
    while b <= n:
        print b,
        a, b = b, a+b

intro()