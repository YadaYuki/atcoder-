from string import ascii_lowercase

def ascii_lowercase_to_idx(c):
    return ord(c) - ord('a')

N  = int(input())
s = list(input())

word_cnt = [0] * len(ascii_lowercase)

for c in s:
    word_cnt[ascii_lowercase_to_idx(c)] += 1

r = N-1
for l in range(N):
    exchange_char = None
    c_l = s[l]
    word_cnt[ascii_lowercase_to_idx(c_l)] -= 1
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
            r -= 1
            break
        r -= 1

print("".join(s))
