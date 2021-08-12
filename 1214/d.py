# REF:https://note.nkmk.me/python-gcd-lcm/
import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

if __name__ == "__main__":
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    white_space_arr = []
    tail = 0
    for i in range(M):
        white_space = A[i] - tail - 1
        if 
        white_space_arr.append(A[i] - tail)