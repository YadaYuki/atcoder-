from  string import ascii_lowercase,ascii_uppercase

s = input()
has_upper = False
has_lower = False
d = {}
unique = True
for c in s:
    if c in ascii_lowercase:
        has_lower = True
    if c in ascii_uppercase:
        has_upper = True
    if c in d:
        unique = False
    d[c] = True

if has_lower and has_upper and unique:
    print("Yes")
else:
    print("No")

