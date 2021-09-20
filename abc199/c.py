N = int(input())
S = list(input())
Q = int(input())
flag = False


def convert_val(idx):
  if idx >= N:
    return idx - N
  else:
    return idx + N


for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 2:
        flag = not flag
    else:
        A, B = A-1, B-1
        if flag:
            A = convert_val(A)
            B = convert_val(B)
        S[A], S[B] = S[B], S[A]


if flag == True:
  S = S[N:2*N] + S[:N]

print("".join(S))

