A,B = input().split()

digit_num = max(len(A),len(B))
A = A.zfill(digit_num)
B = B.zfill(digit_num)

for i in range(digit_num):
    if int(A[i]) + int(B[i]) > 9:
        print("Hard")
        exit(0)
        
print("Easy")

