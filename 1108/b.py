if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    max_gcd = -1
    ans = 0
    for i in range(2,1001):
        GCD = 0
        for j in range(N):
            if A[j] % i == 0:
                GCD += 1
        if max_gcd < GCD:
            max_gcd = GCD
            ans = i
    print(ans)

