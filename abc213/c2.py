# https://scrapbox.io/AtCoderPracticeMemo/C_-_Reorder_Cards
H,W,N = map(int,input().split())

A,B = [],[]

for i in range(N):
    Ai,Bi = map(int,input().split())
    A.append(Ai)
    B.append(Bi)

# 座標圧縮する
unique_A = list(set(A))
unique_B = list(set(B))

unique_A.sort()
unique_B.sort()

def binary_search(arr,target):
    head = -1
    tail = len(arr)
    while abs(tail-head)>1:
        mid = (tail+head)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            head = mid
        else:
            tail = mid

    return -1

for i in range(N):
    A[i] = binary_search(unique_A,A[i])
    B[i] = binary_search(unique_B,B[i])
    print(A[i]+1,B[i]+1)
    
