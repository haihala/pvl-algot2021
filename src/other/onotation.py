def quick_mafs():
    four = 2+2
    three = four-1
    return three


def func1(iterable):
    for _ in iterable:
        quick_mafs()


def func2(iterable):
    for _ in iterable:
        quick_mafs()
    for _ in iterable:
        quick_mafs()
    for _ in iterable:
        quick_mafs()
    for _ in iterable:
        quick_mafs()


def func3(iterable):
    func2(iterable)


def func4(iterable):
    for _ in iterable:
        for _ in iterable:
            quick_mafs()


def func5(iterable):
    for _ in iterable:
        func1(iterable)


def func6(iterable):
    for _ in iterable:
        for _ in range(5):
            quick_mafs()
