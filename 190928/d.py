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

if __name__ == "__main__":
    A,B = map(int,input().split())
    print(1 + len(prime_factorize(math.gcd(A,B))))