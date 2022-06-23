from bisect import bisect_left

def get_abs_of_closest_val(arr,t):
    
    idx = bisect_left(arr, t)
    # 挿入する位置の右側か左側かが最も近い値
    abs_of_closest_val = abs(t-arr[idx-1])
    if idx < len(arr):
        abs_of_closest_val = min(abs_of_closest_val,abs(t-arr[idx]))
    
    return abs_of_closest_val


R,G,B = [],[],[]
N = int(input())
for _ in range(2*N):
    a,c = input().split()
    a = int(a)
    if c == "R":
        R.append(a)
    if c == "G":
        G.append(a)
    if c == "B":
        B.append(a)

while len(B) % 2 == 1:  # Cが偶数個の色になるようにA,B,Cの名前を変える
    B,R,G = R,G,B

if len(R) % 2 == 0:
    print(0)
    exit()

R.sort()
G.sort()

# pattern1:R,Gから一つずつ選ぶ
ans = min([get_abs_of_closest_val(R, g) for g in G])
# pattern2:R,Bから一つ,G,Bから一つ
if B:
    ans = min(ans,min([get_abs_of_closest_val(R, b) for b in B]) + min([get_abs_of_closest_val(G, b) for b in B]))

print(ans)