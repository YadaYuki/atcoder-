package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	var N int
	fmt.Scan(&N)
	// read A
	A := make([]int, N)
	b := make([]byte, 1)
	i := 0
	for os.Stdin.Read(b); b[0] != '\n'; os.Stdin.Read(b) {
		if b[0] == ' ' {
			continue
		}
		a, _ := strconv.Atoi(string(b))
		A[i] = a
		i++
	}
	dp := make([][]int, N)
	for i := 0; i < N; i++ {
		dp[i] = make([]int, 10)
	}

	dp[0][A[0]] = 1
	MOD := 998244353

	for i := 0; i < N-1; i++ {
		for j := 0; j < 10; j++ {
			x := j
			y := A[i+1]
			dp[i+1][(x+y)%10] = (dp[i+1][(x+y)%10] + dp[i][j]) % MOD
			dp[i+1][(x*y)%10] = (dp[i+1][(x*y)%10] + dp[i][j]) % MOD
		}
	}
	for i := 0; i < 10; i++ {
		fmt.Println(dp[N-1][i])
	}
}
