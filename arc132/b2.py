n = int(input())
p = list(map(int, input().split()))

if n == 2:
    print(1)
    exit()

def next_elem(arr,i):
    if i == n-1:
        return arr[0]
    else:
        return arr[i+1]

one_idx = p.index(1)
ascending = next_elem(p,one_idx) == 2
ans = -1
if ascending:
    a_cnt = one_idx
    b_cnt = n - one_idx
    ans = min(a_cnt,b_cnt+2)
else:
    a_cnt = one_idx + 1
    b_cnt = n - a_cnt
    ans = min(a_cnt,b_cnt) + 1

print(ans)