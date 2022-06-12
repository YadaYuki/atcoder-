H,W = map(int,input().split())
c = [list(input()) for _ in range(H)]
COLOR_CANDIDATES = list("12345")
for h in range(H):
    for w in range(W):
        if c[h][w] == '.':
            colors_surrounding = set()
            for hn,wn in [(h-1,w),(h+1,w),(h,w-1),(h,w+1)]:
                if 0<=hn<H and 0<=wn<W:
                    colors_surrounding.add(c[hn][wn])
            for color in COLOR_CANDIDATES:
                if color not in colors_surrounding:
                    c[h][w] = color
                    break


for h in range(H):
    print("".join(c[h]))