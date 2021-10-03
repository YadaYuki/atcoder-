import itertools

S,K = input().split()
K = int(K)

patterns,pattern_dict = [],{}

perm = list(itertools.permutations(S,len(S)))

for i in range(len(perm)):
    pattern = "".join(list(perm[i]))
    if pattern_dict.get(pattern) == None:
        patterns.append(pattern)
        pattern_dict[pattern] = True
        


patterns.sort()
print(patterns[K-1])
