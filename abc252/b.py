N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
max_A = max(A)
max_delicious_foods = []
for i in range(len(A)):
    if A[i] == max_A:
        max_delicious_foods.append(i + 1)

for b in B:
    if b in max_delicious_foods:
        print('Yes')
        exit()
    
print('No')



