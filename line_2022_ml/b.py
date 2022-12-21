import sys

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
memo = {}
def dfs(prev,cur,tree,R,B):
    is_root = (prev == -1)
    if (not is_root) and (len(tree[cur]) == 1):
        r,b = R[cur],B[cur]
        memo[cur][cur] = [r,b]
        gcd_rb = gcd(r,b)
        r,b = r//gcd_rb,b//gcd_rb
        return r,b
    r,b = R[cur],B[cur]
    for ch in tree[cur]:
        if ch == prev:
            continue
        rch,bch = None,None
        if memo[cur][ch] != [-1,-1]:
            rch,bch = memo[cur][ch]
        else:
            rch,bch = dfs(cur,ch,tree,R,B)
            memo[cur][ch] = [r,b]
        r += rch
        b += bch
    
    gcd_rb = gcd(r,b)
    r,b = r//gcd_rb,b//gcd_rb
    return r,b 


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    N = int(lines[0])
    tree = [[] for i in range(N)]
    for i in range(1,N):
        x,y = map(int,lines[i].split())
        tree[y-1].append(x-1)
        tree[x-1].append(y-1)
    R,B = [],[]
    for i in range(N,2*N):
        r,b = map(int,lines[i].split())
        R.append(r)
        B.append(b)
    for i in range(N):
        memo[i] = [[-1,-1] for j in range(N)]
    for i in range(N):
        print(*dfs(-1,i,tree,R,B))
        print(memo)
        



if __name__ == '__main__':
    l = input()
    N = int(l)
    lines = [l]
    for i in range(N*2-1):
        lines.append(input())
    main(lines)

