def get_sum(num):
    return (1 + num) * num / 2

if __name__ == "__main__":
    a,b,c = map(int,input().split())
    ans = int(((get_sum(a)%998244353)*get_sum(b)%998244353)*get_sum(c)%998244353)
    print(ans)
