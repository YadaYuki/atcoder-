from string import ascii_lowercase

N = int(input())
s = list(input())

word_cnt = [0] * len(ascii_lowercase)

def ascii_lowercase_to_idx(c):
    return ord(c) - ord('a')
def idx_to_ascii_lowercase(c):
    return ord(c) - ord('a')

for c in s:
    word_cnt[ascii_lowercase_to_idx(c)] += 1

l = 0
r = N-1

for l in range(N):
    c_l = s[l]
    word_cnt[ascii_lowercase_to_idx(c_l)] -= 1
    exchange_char = None
    for j in range(ascii_lowercase_to_idx(c_l)):
        if word_cnt[j] > 0:
            exchange_char = ascii_lowercase[j]
            break
    if exchange_char is None:
        continue
    
    while r > l:
        word_cnt[ascii_lowercase_to_idx(s[r])] -= 1
        if s[r] == exchange_char:
            s[l], s[r] = s[r], s[l]
            break
        r -= 1

print(''.join(s))

