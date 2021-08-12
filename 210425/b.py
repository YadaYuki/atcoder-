N = int(input())
A = [int(item) for item in input().split()]
B = [int(item) for item in input().split()]
ans = min(B) - max(A) + 1
print(ans if ans > 0 else 0)
