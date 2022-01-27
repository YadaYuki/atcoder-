import math
N = int(input())

price = math.floor(N * 1.08)

if price == 206:
    print("so-so")
elif price < 206:
    print("Yay!")
else:
    print(":(")