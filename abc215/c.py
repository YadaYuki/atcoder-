from  itertools import permutations
S,K = input().split()
K = int(K)

patterns = list(permutations(S))

# to unique
pattern_dict = {}

for pattern in patterns:
    pattern_dict["".join(pattern)] = True

unique_patterns = list(pattern_dict.keys())

unique_patterns.sort()

print(unique_patterns[K-1])
