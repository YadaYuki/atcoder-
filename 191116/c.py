import itertools
def get_distance(city_i,city_j):
    return ((city_i[0]-city_j[0]) ** 2 + (city_i[1]-city_j[1]) ** 2 ) ** 0.5
# itertools.combinations([1,2,3,4])
if __name__ == "__main__":
    N = int(input())
    city_arr = []
    for i in range(N):
        city_arr.append(list(map(int,input().split())))
    
    pattern_arr = list(itertools.permutations([i for i in range(N)]))
    distance_sum = 0
    for pattern in pattern_arr:
        for i in range(1,N):
            distance_sum += get_distance(city_arr[pattern[i-1]],city_arr[pattern[i]])
    print(distance_sum/len(pattern_arr))