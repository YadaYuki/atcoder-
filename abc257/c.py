N = int(input())
S = list(input())
W = list(map(int,input().split()))

adults = []
children = []

for i in  range(N):
    if S[i] == "1":
        adults.append(W[i])
    else:
        children.append(W[i])

if len(adults) == 0 or len(children) == 0:
    print(N)
    exit(0)

max_children = max(children)
min_adults = min(adults)
max_adults = max(adults)
min_children = min(children)

def f(x):
    pred_s = []
    for w in W:
        if w >= x:
            pred_s.append("1")
        else:
            pred_s.append("0")
    fx = 0
    for i in range(N):
        if pred_s[i] == S[i]:
            fx += 1
    # print(pred_s,S,fx)
    return fx

ans = -1
for x in [max_children+0.1,max_children-0.1,min_adults+0.1,min_adults-0.1,max_adults+0.1,max_adults-0.1,min_children+0.1,min_children-0.1]:
    ans = max(f(x),ans)
    # print(x,ans,f(x))


print(ans)