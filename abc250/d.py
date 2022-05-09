import math

def prime_factorize(N):
    prime_arr = []
    while N % 2 == 0:
        N //= 2
        prime_arr.append(2)
    
    prime = 3
    while prime ** 2 <= N:
        if N % prime == 0:
            N //= prime
            prime_arr.append(prime)
        else:
            prime += 2
    if N != 1:
        prime_arr.append(N)
    return prime_arr

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError("n is int-type.")
    if n < 2:
        raise ValueError("n is more than 2")
    data = [i for i in range(2, n + 1)]
    for d in data:
        data = [x for x in data if (x == d or x % d != 0)]
    return data

def is_prime(x:int):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True


N = int(input())
q = []

for p in range(2,int(N ** (1/3)) + 1):
    if is_prime(q):
        pass

