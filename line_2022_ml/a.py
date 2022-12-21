import sys


def is_intersect(l1,l2):
    s,t = 0.0,0.0
    a,b = l1
    c,d = l2
    xa,ya = a
    xb,yb = b
    xc,yc = c
    xd,yd = d

    s = (xa-xb) * (yc-ya) - (ya-yb) * (xc-xa)
    t = (xa-xb) * (yd-ya) - (ya-yb) * (xd-xa)
    if s * t > 0:
        return False
    
    s = (xc - xd) * (ya - yc) - (yc - yd) * (xa - xc)
    t = (xc - xd) * (yb - yc) - (yc - yd) * (xb - xc)
    if s * t > 0:
        return False
    
    return True


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    N,L = map(float,lines[0].split())
    N = int(N)
    line_list = []
    for i, v in enumerate(lines[1:]):
        a,b,c,d = map(float,v.split())
        line_list.append([[a,b],[c,d]])
    
    lines_connected_with_x_axis = set()
    lines_connected_with_y_axis = set()
    for i in range(N):
        lines_intersect_with_i = []
        li = line_list[i]
        for j in range(i):
            lj = line_list[j]
            if is_intersect(li,lj):
                lines_intersect_with_i.append(j)
        i_is_connected_with_x_axis = (li[0][0] == 0.0) or (li[1][0] == 0.0)
        for l in lines_intersect_with_i:
            if l in lines_connected_with_x_axis:
                i_is_connected_with_x_axis = True
                break
        if i_is_connected_with_x_axis:
            lines_connected_with_x_axis.add(i)
            for l in lines_intersect_with_i:
                lines_connected_with_x_axis.add(l)
        
        i_is_connected_with_y_axis = (li[0][1] == 0.0) or (li[1][1] == 0.0)
        for l in lines_intersect_with_i:
            if l in lines_connected_with_y_axis:
                i_is_connected_with_y_axis = True
                break
        if i_is_connected_with_y_axis:
            lines_connected_with_y_axis.add(i)
            for l in lines_intersect_with_i:
                lines_connected_with_y_axis.add(l)

        if i in lines_connected_with_x_axis and i in lines_connected_with_y_axis:
            print("NO")
            print(i+1)
            exit()
    print("YES")
        



    


if __name__ == '__main__':
    l = input()
    N,L = map(float,l.split())
    N = int(N)
    lines = [l]
    for l in range(N):
        lines.append(input())
    main(lines)
