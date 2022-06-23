p = 0

runner_in_bases = [0,0,0,0,0]
N = int(input())
A = list(map(int,input().split()))

for a in A:
    runner_in_bases[0] = 1
    for i in range(3,-1,-1):
        runner_in_bases[min(i+a,4)] += runner_in_bases[i]
        runner_in_bases[i] = 0

print(runner_in_bases[-1])



