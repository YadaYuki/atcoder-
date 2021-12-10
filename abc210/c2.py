from collections import defaultdict

N,K = map(int,input().split())
candy_list = list(map(int,input().split()))

candy_dict = defaultdict(int)

# Init candy_dict

for i in range(K):
    candy_dict[candy_list[i]] += 1

ans = len(candy_dict)
for i in range(1,N-K+1):
    # remove candy_list[i - 1] from candy_dict
    if candy_dict[candy_list[i - 1]] == 1:
        candy_dict.pop(candy_list[i - 1])
    else:
        candy_dict[candy_list[i - 1]] -= 1
    
    # add candy_list[i + K - 1] to candy_dict   
    candy_dict[candy_list[i + K - 1]] += 1

    ans = max(ans, len(candy_dict))


print(ans)