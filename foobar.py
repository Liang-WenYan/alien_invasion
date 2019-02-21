import os


def test(*args):
    for arg in args:
        print(arg)


def test1(args):
    for arg in args:
        print(arg)


test(1, 2, 3, (5, 6))
test1((1, 2, 3, (5, 6)))
test1([1, 2, 3, (5, 6)])
