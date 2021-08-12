import itertools

def get_times_sum(T,pos_arr):
    times_sum = 0
    for i in range(1,len(pos_arr)):
        times_sum += T[pos_arr[i-1]][pos_arr[i]]
    times_sum += T[0][pos_arr[-1]]
    return times_sum


if __name__ == "__main__":
    N,K = map(int,input().split())
    T = [list(map(int,input().split())) for i in range(N)]
    pos_arr = [i for i in range(N)]
    permutations = list(itertools.permutations(pos_arr[1:]))
    count = 0
    permutations = [list(permutation) for permutation in permutations]
    for permutation in permutations:
        pos_arr = [0] + permutation
        if K == get_times_sum(T,pos_arr):
            count += 1
    print(count)

        

        
