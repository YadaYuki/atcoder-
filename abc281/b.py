from string import ascii_uppercase

S = list(input())
if len(S) != 8:
    print("No")
    exit()
c_head,c_tail = S[0],S[-1]
if not (c_head in ascii_uppercase):
    print("No")
    exit()

if not (c_tail in ascii_uppercase):
    print("No")
    exit()

nums = S[1:7]

for n in nums:
    if not (ord("0") <= ord(n) <= ord("9")):
        print("No")
        exit()

num = int("".join(nums))

if not (100000 <= num <= 999999):
    print("No")
    exit()

print("Yes")
