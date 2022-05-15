import math
import statistics


def comb(n,c):
   return math.factorial(n)/(math.factorial(n-c) * math.factorial(c))


def prob(n,i,X):
    if i == 1:
        return (1/X) ** n 
    return (i/X) ** n - ((i-1)/X) ** n

X = 100
mean = 0.0
m = list(map(int,input().split()))
m_mean = statistics.mean(m)
print(m_mean)
for dice_num in range(1,6):
    mean = 0.0
    for i in range(1,X+1):
        p = prob(dice_num,i,X)
        mean += i * p
    print(f'dice_num:{dice_num}')
    print(f'mean:{mean}')

diff = []
