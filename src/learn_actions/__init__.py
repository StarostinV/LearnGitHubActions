import sys


def add(a, b):
    if sys.version_info[1] > 7:
        return a + b
    else:
        return a + b  # test coverage for different versions
