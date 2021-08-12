def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

if __name__ == "__main__":
    A,B = map(int,input().split())
    print(int((A * B) / gcd(A,B)))