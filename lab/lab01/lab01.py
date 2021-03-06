"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    if n ==1:
        return f(x)
    else:
        return repeated(f,n-1,f(x))


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    gw=n%10
    sum=gw
    mid_n=gw
    i=10
    while True:
        temp=(n//i)%10
        mid_n+=i*temp
        sum+=temp
        if mid_n == n:
            return sum
        else:
            i*=10

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    prevNum=n%10
    i=10
    mid_n=prevNum
    while True:
        temp=(n//i)%10
        mid_n+=i*temp
        i*=10
        if temp == 8 and prevNum == temp:
            return True
        else:
            prevNum=temp

        if mid_n == n:
            return False
