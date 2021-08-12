if __name__ == "__main__":
    A,B = map(int,input().split())
    max_follower = 2 * A + 100
    print(max_follower-B)