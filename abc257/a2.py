N,X = map(int,input().split())

alphabets = [chr(ord("A")+i) for i in range(26)]

s = ""

for c in alphabets:
    s += c * N

print(s[X-1])