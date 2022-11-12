N = int(input())
s = set()
ok = True
for i in range(N):
    S = input()
    s.add(S)
    S = list(S)
    if not (S[0] in ["H","D","C","S"]):
        ok = False
    if not (S[1] in ["A", "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]):
        ok = False

if not ok:
    print("No")
    exit()

if len(s) < N:
    print("No")
    exit()

print("Yes")