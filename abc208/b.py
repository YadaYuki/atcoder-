coin_list = [1]


for i in range(9):
    coin_list.append(coin_list[i] * (i + 2))

coin_list.sort(reverse=True)

P = int(input())
ans = 0
for coin in coin_list:
    coin_num = 100
    while coin_num > 0 and coin <= P:
        coin_num -= 1
        P -= coin
        ans += 1

print(ans)


