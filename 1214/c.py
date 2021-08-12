from math import factorial
def f(n,r):
    return factorial(n) / (factorial(r) * factorial(n - r))

if __name__ == "__main__":
    L = int(input())
    print(int(f(L-1,11)))