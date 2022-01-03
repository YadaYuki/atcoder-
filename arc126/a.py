def get_ans(N2,N3,N4):
    ans = 0
    if N4 >= 1 and N3 >= 2: # pattern 1: 10 = 4 * 1 + 3 * 2
        N4_p1 = N4
        N3_p1 = N3 // 2
        p1_num = min(N3_p1,N4_p1)
        ans += p1_num
        N3 -= p1_num * 2
        N4 -= p1_num
    
    if N4 >= 2 and N2 >= 1: # pattern 2: 10 = 4 * 2 + 2 * 1
        N4_p2 = N4 // 2
        N2_p2 = N2
        p2_num = min(N4_p2,N2_p2)
        ans += p2_num
        N4 -= p2_num * 2
        N2 -= p2_num
    
    if N4 >= 1 and N2 >= 3:  # pattern 3: 10 = 4 * 1 + 2 * 3
        N4_p3 = N4 
        N2_p3 = N2 // 3
        p3_num = min(N4_p3,N2_p3)
        ans += p3_num
        N4 -= p3_num 
        N2 -= p3_num * 3
    
    if N3 >= 2 and N2 >= 2:  # pattern 4: 10 = 3 * 2 + 2 * 2
        N3_p4 = N3 // 2
        N2_p4 = N2 // 2
        p4_num = min(N3_p4,N2_p4)
        ans += p4_num
        N3 -= p4_num * 2
        N2 -= p4_num * 2
    
    if N2 >= 5:  # pattern 5: 10 = 2 * 5
        p5_num = N2 // 5
        ans += p5_num

    return ans
    

    





if __name__ == '__main__':
    T = int(input())
    ans = []
    for _ in range(T):
        N2,N3,N4 = map(int,input().split())
        ans.append(get_ans(N2,N3,N4))
    
    for item in ans:
        print(item)
    