import array
import bisect

L,Q = map(int,input().split())
a = array.array("i",[0,L])
for i in range(Q):
  c,x = map(int,input().split())
  y = bisect.bisect(a,x)
  if c == 1:
    a.insert(y,x)
  else:
    print(a[y]-a[y-1])
