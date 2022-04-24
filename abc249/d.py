from collections import OrderedDict

num_dict = OrderedDict({})

N = int(input())
A = list(map(int, input().split()))
A.sort()
for a in A:
    if a in num_dict:
        num_dict[a] += 1
    else:
        num_dict[a] = 1





# 一旦1の場合を無視する
ans = 0

if 1 in num_dict:
    if num_dict[1] >= 3:
        ans += num_dict[1] * (num_dict[1] - 1) * (num_dict[1] - 2) 

# print(num_dict)
for k,v in num_dict.items():
    sqrt_k = int(k**0.5)
    if k == 1:
        continue
    else:
        for kj,vj in num_dict.items():
            if sqrt_k < kj:
                break
            if kj == 1:
                ans += (v-1) * vj * 2
                # print(ans,k,v)
            elif k % kj == 0 and int(k/kj) in num_dict:
                ans += v * vj * num_dict[int(k/kj)] * 2


print(ans)