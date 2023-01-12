N = int(input())
one_bit_digit = list()
for i in range(60):
    if ((N >> i) & 1) == 1:
        one_bit_digit.append(i)

ans = list()
for pattern in range(2**len(one_bit_digit)):
    x = 0
    for b in range(len(one_bit_digit)):
        if ((pattern >> b) & 1) == 1:
            x += 2 ** one_bit_digit[b]
    ans.append(x)


for a in ans:
    print(a)