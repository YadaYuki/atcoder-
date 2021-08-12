def replace_half(S, N):
    first_half, second_half = S[:N], S[N:]
    return second_half + first_half


def replace_char(S, A, B):
    list_s = list(S)
    list_s[A], list_s[B] = list_s[B], list_s[A]
    return "".join(list_s)


N = int(input())
S = input()
Q = int(input())
a = 0
for i in range(Q):
    T, A, B = [int(item) - 1 for item in input().split()]
    if T == 0:
        S = replace_char(S, A, B)
    elif T == 1:
        a += 1

S = S if a % 2 == 0 else replace_half(S, N)

print(S)
