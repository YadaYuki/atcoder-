if __name__ == "__main__":
    N,M,T = map(int,input().split())
    MAX_N = N
    time_point_arr = [0]
    for i in range(M):
        time_point_arr.extend(list(map(int,input().split())))
    time_point_arr.append(T)
    for i in range(len(time_point_arr)-1):
        if i % 2 == 0: # outdoor
            N -= (time_point_arr[i+1] - time_point_arr[i])
        else : 
            N = min(MAX_N,N+((time_point_arr[i+1] - time_point_arr[i])))
        if N <= 0:
            print("No")
            exit(0)
        
    print("Yes")
