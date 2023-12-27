import functools

def get_exercise_number():
    return 7


def sieve(n):
    primes = []
    count = 0
    i = 2
    while count < n:
        # is_prime = functools.reduce(lambda x, b: b and i % x != 0, primes, True)
        is_prime2 = True
        for p in primes:
            if i % p == 0:
                is_prime2 = False
                break
        if is_prime2:
            count += 1
            primes.append(i)
        i += 1
    return primes[-1]


def solve(n=10_001):
    return sieve(n)
