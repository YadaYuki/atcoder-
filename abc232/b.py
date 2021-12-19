S = list(input())
T = list(input())

diff_map = {}


for i in range(len(S)):
    c_T, c_S = T[i], S[i]
    diff = ord(c_T) - ord(c_S)
    if diff  < 0:
        diff = 26 + diff
    diff_map[diff] = True

if len(diff_map) == 1:
    print("Yes")
else:
    print("No")

