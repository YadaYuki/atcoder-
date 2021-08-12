a = [1,0,5]
for i in range(2,50):
  a.append(a[i-2] + a[i-1] + a[i])
  print(a)

print(a[29])