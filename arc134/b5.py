from string import ascii_lowercase
N = int(input())
s = list(input())

word_cnt = [0] * 26


def char_idx(c):
    return ord(c) - ord('a')
for c in s:
    word_cnt[char_idx(c)] += 1

r = N - 1
for l in range(N):
    c_l = s[l]
    word_cnt[char_idx(c_l)] -= 1
    c_r = None
    for c in range(char_idx(c_l)):
        if word_cnt[c] > 0:
            c_r = ascii_lowercase[c]
            break
    if c_r is None:
        continue
    while r > l:
        word_cnt[char_idx(s[r])] -= 1
        if s[r] == c_r:
            s[l], s[r] = s[r], s[l]
            r -= 1
            break
        r -= 1

print(''.join(s))


