""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a % b == 0:
        return b
    elif a < b:
        return gcd(b,a)
    else:
        return gcd(b,a%b)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count=1
    def count_hailstone(n):
        nonlocal count
        print(n)
        if n == 1:
            return count
        elif n % 2 == 0:
            count+=1
            return count_hailstone(n//2)
        else:
            count+=1
            return count_hailstone(n*3+1)
    return count_hailstone(n)
        
