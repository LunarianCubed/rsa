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

def encrypt(plaintext, PR):

    return plaintext


def decrypt(ciphertext, PU):

    return ciphertext

def main():
    a = 100
    print(findPrime(1000, 10000, 10))
    print(findPrime(1000, 10000, 19))


if __name__ == "__main__":
    main()
