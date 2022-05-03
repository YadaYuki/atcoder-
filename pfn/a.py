def int_to_bin(n):
    return bin(n)[2:]

def solve(N,X):
    X_bin = int_to_bin(X)
    if len(X_bin) <= N:
        # Xを2進数表記した際のビット数がN桁以下ならば、「Xを2進数表記した際の"1"の登場回数 = ボタンを押す回数」
        return X_bin.count("1")
    else:
        # N桁以上の場合は、N桁以上のビットを、2^(N-1)のボタンで満たすのが最適
        X_bin_reversed = list(reversed(X_bin))
        ans = X_bin_reversed[:N].count("1")
        for i in range(N,len(X_bin_reversed)):
            if X_bin_reversed[i] == "1":
                ans += 2 ** (i-N+1)
        return ans


N,X = map(int,input().split())
print(solve(N,X))