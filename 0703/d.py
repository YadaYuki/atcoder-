from typing import List


def get_median_of_height(height_arr: List[int]) -> int:
    return sorted(height_arr)[int((len(height_arr)-1)/2)]


def main(park_mat: List[List[int]], N: int, K: int):
    # sub matrix
    sub_mat_indexes = []
    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            sub_mat_indexes.append([i, j])
    
    min_median = float("inf")
    for sub_mat_index in sub_mat_indexes:
      height_array = []
      i_start,j_start = sub_mat_index
      for i in range(i_start,i_start+K):
        for j in range(j_start,j_start+K):
          height_array.append(park_mat[i][j])
      min_median = min(min_median,get_median_of_height(height_array))

    print(min_median)


if __name__ == "__main__":
    N, K = [int(item) for item in input().split()]
    park_mat = [[int(item) for item in input().split()] for _ in range(N) ]
    main(park_mat,N,K)
    # print(get_median_of_height([1,7,5,8]))
    # print(get_median_of_height([1,7,2,8,3]))
    
