A,B,K = map(int,input().split())

shout = 0
while A < B:
    A *= K
    shout += 1
print(shout)