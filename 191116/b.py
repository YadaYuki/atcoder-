if __name__ == "__main__":
    N = int(input())
    S = input()
    if N%2 == 1:
        print("No")
    else:
        if S[:int(N/2)] == S[int(N/2):N]:
            print("Yes")
        else:
            print("No")
