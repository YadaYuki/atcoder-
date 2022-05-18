X = list(input())

acc = [int(X[0])]

for b in X[1:]:
    acc.append(acc[-1] + int(b))

acc.reverse()

ans = ""
MAX_ANS = 10 ** 6 
ans = [0] * MAX_ANS
for i in range(len(X)):
    ans[i] += acc[i]
    ans[i+1] += ans[i] // 10
    ans[i] = ans[i] % 10


ans.reverse()

is_zero = True
output = ""
for i in ans:
    if i != 0 and is_zero:
        is_zero = False
        output = output +  str(i)
    elif is_zero == False:
        output = output + str(i)
    

print(output)