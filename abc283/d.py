
from collections import defaultdict
from string import ascii_lowercase
S = list(input())
j_stack = list()
for alphabet in ascii_lowercase:
    alphabet_appeared = -1
    for i,c in enumerate(S):
        if c == "(":
            j_stack.append(i)
        if c == ")":
            j = j_stack.pop()
            if j < alphabet_appeared < i:
                alphabet_appeared = -1
        if c == alphabet:
            if alphabet_appeared != -1:
                print("No")
                exit()
            else:
                alphabet_appeared = i

print("Yes")