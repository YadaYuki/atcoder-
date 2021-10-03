S = input()
T = input()
if S == T:
    print("Yes")
    exit()

for i in range(len(S)-1):
    S_exchanged = list(S)
    S_exchanged[i],S_exchanged[i+1] = S_exchanged[i+1],S_exchanged[i]
    if "".join(S_exchanged) == T:
        print("Yes")
        exit()

print("No")
