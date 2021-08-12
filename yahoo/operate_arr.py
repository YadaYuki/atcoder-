
def query_one(arr, i, x):
    arr[i] = x


def query_two(arr, l, r, s, t):
    count = 0
    for i in range(l, r):
        if s <= arr[i] <= t:
            count += 1
    return count


def main(lines):
    arr = [int(item) for item in lines[1].split()]
    q = int(lines[2])
    for i in range(3, q+3):
        query_arr = [int(item) for item in lines[i].split(" ")]
        query_type = query_arr[0]
        if query_type == 1:
            i, x = query_arr[1:]
            query_one(arr, i-1, x)
        if query_type == 2:
            l, r, s, t = query_arr[1:]
            print(query_two(arr, l-1, r, s, t))

    # print(arr)


if __name__ == "__main__":
    lines = [
        "3",
        "3 1 5",
        "3",
        "2 1 3 1 1000",
        "1 2 10000",
        "2 1 3 1 1000",
    ]
    main(lines)
    lines = [
        "3",
        "2 4 8",
        "4",
        "2 2 3 5 7",
        "2 2 3 5 8",
        "2 2 3 5 9",
        "2 1 3 1 6",
    ]
    main(lines)
