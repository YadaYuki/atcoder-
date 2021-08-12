if __name__ == "__main__":
    N,X = map(int,input().split())
    S = input()
    for i in range(N):
        if S[i] == "x":
            X -= 1
        else:
            X += 1
    print(X)