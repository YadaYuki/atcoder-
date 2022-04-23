A,B,C,D,E,F,X = map(int,input().split())
takahashi = (X // (A+C))* A * B
a = X % (A+C)
if a > A:
    a = A

takahashi += a * B

aoki = (X // (D+F))* D * E
a = X % (D+F)
if a > D:
    a = D
aoki += a * E


if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
