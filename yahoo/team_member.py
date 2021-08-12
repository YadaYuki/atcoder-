import itertools

MORALE_UP, MORALE_DOWN = ".", "S"


def get_member_num_morale_up(n, k, s):
    if s.count(MORALE_DOWN) < k:
        return n
    else:
      s = list(s)
      moral_down_idx  = [i for i in range(len(s)) if s[i] == MORALE_DOWN]
      patterns = list(itertools.combinations(moral_down_idx,k))
      ans = -1
      for pattern in patterns:
        s_temp = s.copy()
        for i in pattern:
          if i+1 < n:
            s_temp[i+1] = MORALE_UP
          if i-1 >= 0:
            s_temp[i-1] = MORALE_UP
          s_temp[i] = MORALE_UP
        ans = max(ans,s_temp.count(MORALE_UP))
      return ans


def main(lines):
    n, k = [int(item) for item in lines[0].split()]
    s = lines[1]
    print(get_member_num_morale_up(n, k, s))


if __name__ == "__main__":
    lines = [
        "5 3",
        "....."
    ]
    main(lines)
    lines = [
        "5 1",
        "SS..S"
    ]
    main(lines)
