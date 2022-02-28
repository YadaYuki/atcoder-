T = int(input())


def solve_query(a,s):
    min_x = min_y = a
    left = s - (min_x+min_y)
    bit_num = 61
    if left < 0:
        return False
    else:
        
        return left & a == 0
                
ans= []
for _ in range(T):
    a,s = map(int,input().split())
    if solve_query(a,s):
        ans.append('Yes')
    else:
        ans.append('No')

for i in ans:
    print(i)