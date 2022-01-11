N = int(input())

coin = 0

for i in range(10**9):
    coin += (i+1)
    if coin >= N:
        break

print(i+1)