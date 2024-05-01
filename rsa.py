#! /bin/python3
import math
import random


# This function test if a number is prime
# parameter: @x: int
# return bool
# Not used in this program but required for the assignment
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (n + 2) == 0:
            return False
    return True


# This function finds (n)th prime number
# between low and high
def find_prime(low: int, high: int, n: int):
    prime = sieve(low, high)
    if len(prime) >= n:
        return prime[n - 1]
    else:
        return None


# Return @primes:array
# as a list of prime numbers between @low and  @limit
def sieve(low: int, limit: int):
    isPrime = [True] * (limit + 1)
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if isPrime[i]:
            j = 2
            while (i * j) < (limit + 1):
                isPrime[i * j] = False
                j = j + 1

    primes = []
    for i in range(low, limit + 1):
        if isPrime[i]:
            primes.append(i)
    return primes


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# This function use extended Euclidean algorithm
# to find the modular inverse @d of @e
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


def encrypt(plaintext, PR):
    d, p, q = PR
    return pow(int(letter_to_number(plaintext)), d, p * q)


def decrypt(ciphertext, PU):
    e, n = PU
    plain_number = pow(ciphertext, e, n)
    return number_to_letter(str(plain_number))


def generate_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # e = 2
    # Random e was disabled for testing
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
        else:
            e = e + 1

    exgcd, x, y = extended_gcd(e, phi)
    d = x % phi
    return (e, n), (d, p, q)


def letter_to_number(string):
    result = ""
    for letter in string.lower():
        result += "{:02d}".format(ord(letter) - ord('a'))
    return result


def number_to_letter(string):
    result = ""
    for i in range(0, len(string), 2):
        result += chr(int(string[i:i + 2]) + ord('a'))
    return result


def main():
    default = input("Do you want to use default values? (Y/N)\n")
    if default.lower() == "y":
        plaintext = "rsa"
        p = find_prime(1000, 10000, 10)
        q = find_prime(1000, 10000, 19)

    else:
        print("pick a p as the (n)th prime number between x and y:")
        n = int(input("Enter n: "))
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        p = find_prime(x, y, n)
        if p is None:
            print("there is no %dth prime number between %d and %d" % (n, x, y))
            return

        print("pick a p as the (n)th prime number between x and y:")
        n = int(input("Enter n: "))
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        q = find_prime(x, y, n)
        if q is None:
            print("there is no %dth prime number between %d and %d" % (n, x, y))
            return

        plaintext = input("Enter plaintext: ")

    PU, PR = generate_key(p, q)
    print("Public key: \n\t{{{}, {}}}".format(PU[0], PU[1]))
    print("Private key: \n\t{{{}, {}, {}}}".format(PR[0], PR[1], PR[2]))

    print("ciphertext: \n\t" + str(encrypt(plaintext, PR)))
    print("plaintext: \n\t" + decrypt(encrypt(plaintext, PR), PU))


if __name__ == "__main__":
    main()
