package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	fmt.Scan(&N)
	var X, Y int
	fmt.Scan(&X, &Y)
	A := make([]int, N)
	B := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i], &B[i])
	}
	INF := 1000000000
	dp := make([][][]int, N+1)
	for i := 0; i < N+1; i++ {
		dp[i] = make([][]int, X+1)
		for j := 0; j < X+1; j++ {
			dp[i][j] = make([]int, Y+1)
			for k := 0; k < Y+1; k++ {
				dp[i][j][k] = INF
			}
		}
	}
	for i := 0; i < N+1; i++ {
		dp[i][0][0] = 0
	}

	for i := 1; i < N+1; i++ {
		for j := 0; j < X+1; j++ {
			for k := 0; k < Y+1; k++ {
				xx := int(math.Min(float64(X), float64(j+A[i-1])))
				yy := int(math.Min(float64(Y), float64(k+B[i-1])))
				dp[i][xx][yy] = int(math.Min(float64(dp[i][xx][yy]), float64(dp[i-1][j][k]+1)))
				dp[i][j][k] = int(math.Min(float64(dp[i][j][k]), float64(dp[i-1][j][k])))
			}
		}
	}

	if dp[N][X][Y] == INF {
		fmt.Println(-1)
	} else {
		fmt.Println(dp[N][X][Y])
	}
}
