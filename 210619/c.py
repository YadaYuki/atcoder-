
def main(N, A):
    ans = int(A[0] != A[1])
    if N == 2:
        print(ans)
        return
    if ans == 0:
        num_dict = {A[0]: 2}
    else:
        num_dict = {A[0]: 1, A[1]: 1}
    for i in range(2, N):
        if num_dict.get(A[i]) != None:
            ans = ans + (i) - num_dict[A[i]]
            num_dict[A[i]] += 1
        else:
            ans = ans + i
            num_dict[A[i]] = 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    main(N, A)
