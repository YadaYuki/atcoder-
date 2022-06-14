from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

palindrome_c_pairs = defaultdict(bool)

for i in range(N//2):
    if A[i] != A[N-1-i]:
        palindrome_c_pairs[] = True
    

ans = len(palindrome_c_pairs)

print(ans)
