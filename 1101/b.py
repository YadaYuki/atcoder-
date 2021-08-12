def get_sum(a,b):
    return (a+b)*(b-a+1)/2

if __name__ == "__main__":
    N = int(input())
    ans = 0
    for i in range(N):
        a,b = map(int,input().split())
        ans += get_sum(a,b)
    print(int(ans))
