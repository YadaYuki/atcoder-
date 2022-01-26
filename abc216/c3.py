N = int(input())
N_bin = list(bin(N))[2:]
N_bin.reverse()

ans = ''
B_count = 0

for i,bit in enumerate(N_bin):
    if bit == '1':
        addtional_B_count = i - B_count
        ans = 'A' + ('B' * addtional_B_count) + ans
        B_count += addtional_B_count

print(ans)