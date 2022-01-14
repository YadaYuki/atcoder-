from collections import defaultdict

N = int(input())
candidates_dict = defaultdict(int)

for _ in range(N):
    candidates_dict[input()] += 1


ans = -1
ans_candidate = ''

for candidate, count in candidates_dict.items():
    if ans < count:
        ans = count
        ans_candidate = candidate

print(ans_candidate)