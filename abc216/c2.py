N = int(input())

N_bin = list(bin(N))[2:]

ans = ''
cur_B_count = 0
N_bin.reverse()
for i,bit in enumerate(N_bin):
    if bit == '1':
        ans += 'A' 
        for j in range(cur_B_count,i):
            ans += 'B'
        cur_B_count = i


print(ans)
