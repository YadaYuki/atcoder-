def get_norm(vector):
    return (vector[0]**2 + vector[1]**2)**0.5
def is_straight(a,b,c):
    ab = (b[0]-a[0],b[1]-a[1])
    bc = (c[0]-b[0],c[1]-b[1])
    ab_norm,bc_norm = get_norm(ab),get_norm(bc)
    ab_dir_vector = (ab[0]/ab_norm,ab[1]/ab_norm)
    bc_dir_vector = (bc[0]/bc_norm,bc[1]/bc_norm)
    if ab_dir_vector == bc_dir_vector or (ab_dir_vector[0]*(-1),ab_dir_vector[1]*(-1)) == bc_dir_vector:
        return True
    return False

if __name__ == "__main__":
    N = int(input())
    pos_arr = []
    for i in range(N):
        pos_arr.append(tuple(map(int,input().split())))
    
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if is_straight(pos_arr[i],pos_arr[j],pos_arr[k]) == True:
                    print("Yes")
                    exit(0)
    print("No")
            
