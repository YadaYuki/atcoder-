from  string import ascii_lowercase

def char_to_idx(c):
    return ord(c) - ord('a')

N = int(input())
S = list(input())
cnt = [0] * len(ascii_lowercase)
for c in S:
    cnt[char_to_idx(c)] += 1

l = 0
r = N
for l in range(N):
    
    c = char_to_idx(S[l])
    cnt[c] -= 1
    exchange_char = None
    for j in range(c):
        if cnt[j] > 0:
            exchange_char = ascii_lowercase[j]
            break
    if exchange_char is None:
        continue

    while r > l:
        r -= 1
        cnt[char_to_idx(S[r])] -= 1
        if S[r] == exchange_char:
            S[l], S[r] = S[r], S[l]
            break
    if r <= l:
        break
    

print(''.join(S))