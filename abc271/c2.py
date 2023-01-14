from bisect import bisect_left
from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))
id_to_cnt = defaultdict(int)
id_to_ex = defaultdict(bool)
for ai in a:
    id_to_cnt[ai] += 1
    id_to_ex[ai] = True

surplus_books = 0
for k,v in id_to_cnt.items():
    surplus_books += v - 1
a_set = set(a)
a = sorted(list(a_set))

for comic in range(1,N+1):
    if not id_to_ex[comic]:
        if surplus_books >= 2:
            surplus_books -= 2
        elif surplus_books == 1:
            surplus_books = 0
            # これから読もうとしているcomicより、先のcomicが何個あるか
            left_comic = len(a) - bisect_left(a, comic)
            if left_comic == 0:
                print(comic-1)
                exit()
            id_to_ex[a.pop()] = False
        else:
            left_comic = len(a) - bisect_left(a, comic)
            if left_comic < 2:
                print(comic-1)
                exit()
            id_to_ex[a.pop()] = False
            id_to_ex[a.pop()] = False


print(N)


