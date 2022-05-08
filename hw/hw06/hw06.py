from select import select


passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value
        self.previous = None

    def next(self):
        new = Fib()
        new.previous = self
        if not self.previous:
            new.value = 1
        else:
            new.value = new.previous.value + new.previous.previous.value
        return new

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price
        self.stock = 0
        self.balance = 0
    
    def vend(self):
        if self.stock == 0:
            return "Machine is out of stock."
        
        if self.balance < self.price:
            return "You must deposit ${0} more.".format(self.price - self.balance)
        
        change = self.balance - self.price
        self.balance = 0
        self.stock -= 1
        if change == 0:
            return "Here is your {0}.".format(self.product_name)
        else:
            return "Here is your {0} and ${1} change.".format(self.product_name,change)

    def deposit(self,amount):
        if self.stock == 0:
            return "Machine is out of stock. Here is your ${0}.".format(amount)
        
        self.balance += amount
        return "Current balance: ${0}".format(self.balance)

    def restock(self,amount):
        self.stock += amount
        return "Current {0} stock: {1}".format(self.product_name,self.stock)