N = int(input())
s = input()
S = list(s)
x = []
for i in range(N-2):
    if "".join(S[i:i+3]) == "ARC":
        l,r = i,i+2
        while l - 1 >= 0 and S[l-1] == "A":
            l -= 1
        while r + 1 < N and s[r + 1] == "C":
            r += 1
        a_cnt = i - l + 1
        c_cnt = r - (i+1)
        x.append(min(a_cnt,c_cnt))
        
ans = min(sum(x),2*len(x))
print(ans)