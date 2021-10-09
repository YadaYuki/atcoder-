N = input()
digit_num = len(N)
N = int(N)

# 桁数の半分の数値を探索していく
half_digit_max = 10 ** int(digit_num/2)

ans = 0
for i in range(1,half_digit_max):
    cur_digit = len(str(i))
    cur_num = i + i * 10 ** cur_digit
    if cur_num > N:
        break
    ans += 1
print(ans)




