
form math import isqrt

# This function test if a number is prime
# parameter: @x: int
# return bool
def isPrime(x: int ) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = sqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (n + 2) == 0:
            return False
    return True


# This function finds nth prime number
# between low and high
def findPrime(low :int, high: int, n: int) -> int:
    primeList = range(low, high)
    for factor in range(2, low):
        for index in range(0, (high - low)):
            if (number % factor == 0):
                



    return 


def encrypt()

