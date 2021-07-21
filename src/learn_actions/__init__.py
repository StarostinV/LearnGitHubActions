import sys


def add(a, b):
    if sys.version_info[1] > 7:
        return a + b
    else:
        return a + b  # test coverage for different versions

    
    
def add2(a, b):
    """
    Test coverage with docstring
    
    >>> add2(1, 2)
    3
    """
    
    return a + b
