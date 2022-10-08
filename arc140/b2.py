N = int(input())
S = list(input())

xs = []

for i in range(N-2):
    s = "".join(S[i:i+3])
    if s == "ARC":
        # パターンA...ARC...Cを満たしている最大のものを探す
        l = i
        r = i + 2
        diff = 0
        while S[l] == "A" and S[r] == "C":
            l -= 1
            r += 1
            diff += 1

            if l == -1 or r == N:
                break
        xs.append(diff)

print(min(2*len(xs),sum(xs)))