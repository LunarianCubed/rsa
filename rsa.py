#! /bin/python3
from math import isqrt;

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


# This function finds (n)th prime number
# between low and high
def findPrime(low :int, high: int, n: int) -> int:
    prime = sieve(low, high)
    if len(prime) >= n:
        return prime[n - 1]
    else:
        return None


#Return @primes:array
# as a list of prime numbers between @low and  @limit
def sieve(low, limit: int):
    isPrime = [True] * (limit + 1)
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, int (limit ** 0.5) + 1):
        if (isPrime[i]):
            j = 2
            while (i * j) < (limit + 1):
                isPrime[i*j] = False
                j = j + 1

    primes = []
    for i in range(low, limit):
        if (isPrime[i]):
            primes.append(i)
    return primes


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a%b)
        return (gcd, y m x - (a // b) * y)


def encrypt(plaintext, PR):
    d, p, q = PR
    return [pow(ord(char) - ord('a'), d, p * q) for char in plaintext]


def decrypt(ciphertext, PU):
    e, n = PU

def generate_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    gcd, x, y = extended_gcd(e, phi)
    d = x % phi
    return ((e, n), (d, p, q))


def letterToNumber(string):
    result = ""
    for letter in string:
        result += "{:02d}".format(ord(lower(letter)) - ord('a'))
    return result

def main():
    plaintext = "rsa"

    p = findPrime(1000, 10000, 10)
    q = findPrime(1000, 10000, 19)

    PU , PR = generate_key(p, q)

if __name__ == "__main__":
    main()
