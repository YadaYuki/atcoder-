# やっぱARCはデータ構造ゲーではなく、考える系がメインだから面白いよなぁ...。
N = int(input())
S = list(input())
possible_process_counts_for_blocks = []
for i in range(N-2):
    s = "".join(S[i:i+3]) # ある区間の3文字
    if s == "ARC": # processable block
        l = i
        r = i + 2
        while l >= 0 and S[l] == "A":
            l -= 1
        a_cnt = i - l 
        print(l)
        while r <= N - 1 and S[r] == "C":
            r += 1
        c_cnt = r - (i+2) 
        possible_process_count = min(a_cnt,c_cnt) # ブロックに対して、操作可能な上限数
        possible_process_counts_for_blocks.append(possible_process_count)


ans = min(len(possible_process_counts_for_blocks)*2,sum(possible_process_counts_for_blocks))
print(ans)