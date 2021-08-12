N, K = map(int, input().split())
c = list(map(int, input().split()))
candy_dict = {}

for i in range(K):
    candy_color = c[i]
    if candy_dict.get(candy_color) != None:
        candy_dict[candy_color] += 1
    else:
        candy_dict[candy_color] = 1

ans = len(candy_dict)

for i in range(1, N-K+1):
    candy_dict[c[i+K-1]] = 1 if candy_dict.get(c[i+K-1]) == None else candy_dict[c[i+K-1]] + 1
    candy_color = c[i-1]
    if candy_dict[candy_color] == 1:
        candy_dict.pop(candy_color)
    else:
        candy_dict[candy_color] -= 1
    ans = max(len(candy_dict), ans)

print(ans)
