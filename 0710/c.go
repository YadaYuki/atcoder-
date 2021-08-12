package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	N, _ := strconv.ParseInt(scanner.Text(), 0, 64)
	scanner.Scan()
	s := strings.Fields(scanner.Text())
	C := []int64{}
	var i int64
	for i = 0; i < N; i++ {
		item, _ := strconv.ParseInt(s[i], 0, 64)
		C = append(C, item)
	}
	sort.Slice(C, func(i, j int) bool { return C[i] < C[j] })
	divideNum := int64(math.Pow(10, 9))
	divideNum = divideNum + 7
	var ans int64 = 1
	for i = 0; i < N; i++ {
		if C[i]-i <= 0 {
			fmt.Println(0)
			os.Exit(0)
		}
		ans *= C[i] - i
		if ans > divideNum {
			ans %= divideNum
		}
	}
	fmt.Println(ans % divideNum)
}
