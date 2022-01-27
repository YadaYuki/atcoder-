X,Y = map(int,input().split())

diff = Y - X

if diff <= 0:
    print(0)
else:
    if diff % 10 == 0:
        print(diff//10)
    else:
        print(diff//10 + 1)
