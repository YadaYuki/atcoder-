N,A,X,Y = map(int,input().split())
price = 0
if N > A :
  price = X * A + Y * (N - A)
else:
  price = X * N 
print(price)
