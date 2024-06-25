class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity must be a non-negative number')
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return '🍪' * self.cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError(
                'The number of cookies to deposit must be a non-negative number')
        if self.cookies + n > self._capacity:
            raise ValueError(
                'Could not deposit cookies. The number of cookies exceeds capacity')
        self.cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError(
                'The number of cookies to withdraw must be a non-negative number')
        if self.cookies - n < 0:
            raise ValueError(
                'Could not withdraw cookies. Not enough cookies in a jar.')
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
