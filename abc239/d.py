A,B,C,D = map(int,input().split())

def is_prime(x:int):
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

# A~Bのカードの中に高橋くんが必勝できるカードが存在するかどうかを判定する

can_win_takahashi = False
for i in range(A,B+1):
    can_win_takahashi_card = True
    # 高橋くんが出したカードiに対して,青木くんが持っている手持ちのカードで勝てるかどうかを判定
    for j in range(C,D+1):
        if is_prime(i+j): # 素数にできるカードを青木くんが持っている場合、高橋くんは勝てない
            can_win_takahashi_card = False
            break
    can_win_takahashi = can_win_takahashi or can_win_takahashi_card



if can_win_takahashi:
    print("Takahashi")
else:
    print("Aoki")