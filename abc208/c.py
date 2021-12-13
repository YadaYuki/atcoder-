from collections import OrderedDict
N,K = map(int,input().split())
a = list(map(int,input().split()))

candy_dict = OrderedDict()
base_candy_num = K//N
# set base candy
for i in range(N):
    candy_dict[a[i]] = base_candy_num


left_candy_num = K%N
a.sort()
# 国民番号が小さい人から順番に、left_candy_num個のキャンディを一つずつ配布する.
for i in range(left_candy_num):
    candy_dict[a[i]] += 1

for key,value in candy_dict.items():
    print(value)


