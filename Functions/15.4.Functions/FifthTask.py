import math


def a1(number):
    return number ** 2


def a2(number):
    return number ** 3


def a3(number):
    return math.sqrt(abs(number))


def a4(number):
    return abs(number)


def a5(number):
    return math.sin(number)


commands = {'квадрат': a1, 'куб': a2, 'корень': a3, 'модуль': a4, 'синус': a5}
n = int(input())
s = input()
print(commands[s](n))