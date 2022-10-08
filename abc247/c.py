def solve(N:int):
    if N == 1:
        return "1"
    else:
        both_ends = solve(N-1)
        return both_ends + f" {N} " + both_ends
    
if __name__ == '__main__':
    N = int(input())
    print(solve(N))