S,T,X = map(int,input().split())
time = S
while time != T:
    if time == X:
        print("Yes")
        exit(0)
    time += 1
    if time == 24:
        time = 0
print("No")