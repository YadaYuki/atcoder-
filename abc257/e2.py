N = int(input())
C = list(map(int,input().split()))
C = [1e10] + C
min_C = min(C)
d = N // min_C
ans = []
for i in range(d):
    for digit in range(9,0,-1):
        left_digit = d - i - 1 
        left_money = N - C[digit]
        left_digit_can_fill_left_money = (left_digit * min_C <= left_money)
        if left_digit_can_fill_left_money:
            N = left_money
            ans.append(f"{digit}")
            break

print("".join(ans))

