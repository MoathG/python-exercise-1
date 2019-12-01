import doctest
def sum (a,b):
    """
    Calculates the sum of a and b
    >>> sum (1,1)
    5
    >>> sum(1,-1)
    0
    >>> sum (-1,-1)
    -2
    >>> sum(0,-10)
    -10
    >>>
    """
    return a+b

if __name__=="__main__":
    doctest.testmod(verbose=True)
    