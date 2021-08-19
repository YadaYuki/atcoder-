
def main(H: int, W: int, N: int, AB):  # AB: [[A1,B1],[A2,B2],[A3,B3]....]
    column_has_number_arr, count_number_has_column = [True] * W, []

    for i in range(N):
        A, B = AB[i]
        column_has_number_arr[B-1] = False

    count_column = 0
    for i in range(W):
        count_number_has_column.append(count_column)
        count_column += int(column_has_number_arr[i])

    row_has_number_arr, count_number_has_row = [True] * H, []
    for i in range(N):
        A, B = AB[i]
        row_has_number_arr[A-1] = False

    count_row = 0
    for i in range(H):
        count_number_has_row.append(count_row)
        count_row += int(row_has_number_arr[i])

    for i in range(N):
        A, B = AB[i]
        print("{} {}".format(A-count_number_has_row[A-1], B-count_number_has_column[B-1]))

def main_ans(H,W,N,AB):
  A,B = [],[]
  for i in range(N):
    A_i,B_i = AB[i]
    A.append(A_i)
    B.append(B_i)

  X_dict = {x:i+1 for i,x in enumerate(list(sorted(set(A))))} 
  Y_dict = {y:i+1 for i,y in enumerate(list(sorted(set(B))))} 

  for i in range(N):
    print(X_dict[A[i]],Y_dict[B[i]])


if __name__ == "__main__":
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    main_ans(H, W, N, AB)



