from  string import ascii_lowercase

def char_to_idx(c):
    return ord(c) - ord('a')

N = int(input())
S = list(input())
cnt = [0] * len(ascii_lowercase)
for c in S:
    cnt[char_to_idx(c)] += 1

l = 0
r = N-1

while l < r:
    cnt[char_to_idx(S[l])] -= 1
    exchange_char = None
    for i in range(char_to_idx(S[l])):
        if cnt[i] > 0:
            exchange_char = ascii_lowercase[i]
            break
    if exchange_char is None:
        l += 1
        continue
    while S[r] != exchange_char and r > l:
        r -= 1
    S[l], S[r] = S[r], S[l]
    cnt[char_to_idx(exchange_char)] -= 1

print(cnt)
print(''.join(S))