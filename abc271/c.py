import bisect
from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1
a_uniq = sorted(list(set(a)))
extra_comic_cnt = 0
for k,v in d.items():
    extra_comic_cnt += v - 1

if sorted(a) == [i for i in range(1,N+1)]:
    print(N)
    exit()


for cur_comic in range(1,N+1): # 最大でも読めるのはN+1
    idx = bisect.bisect_left(a_uniq, cur_comic)
    if idx != len(a_uniq) and a_uniq[idx] == cur_comic: # cur_comicより大きい要素が存在しない
        continue
    if extra_comic_cnt >= 2:
        extra_comic_cnt -= 2
    elif extra_comic_cnt == 1:
        if bisect.bisect_left(a_uniq, cur_comic) == len(a_uniq): # cur_comicより大きい要素が存在しない
            break
        a_uniq.pop()
        extra_comic_cnt = 0
    else:
        if bisect.bisect_left(a_uniq, cur_comic) == len(a_uniq): # cur_comicより大きい要素が存在しない
            break
        a_uniq.pop()
        if bisect.bisect_left(a_uniq, cur_comic) == len(a_uniq): # cur_comicより大きい要素が存在しない
            break
        a_uniq.pop()
    


print(cur_comic - 1)