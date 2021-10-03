N = int(input())


ans = ""
while N > 0:
    if N % 2 == 1:
        N -= 1
        ans += "A"
    else:
        N = int(N/2)
        ans += "B"

print(ans[::-1])
        
