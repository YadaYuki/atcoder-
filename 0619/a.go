package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func nextFloat(sc *bufio.Scanner) float64 {
	sc.Scan()
	i, e := strconv.ParseFloat(sc.Text(), 64)
	if e != nil {
		panic(e)
	}
	return i
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	N := nextFloat(sc)
	if math.Floor(N*1.08) < 206 {
		fmt.Println("Yay!")
	} else if math.Floor(N*1.08) == 206 {
		fmt.Println("so-so")
	} else {
		fmt.Println(":(")
	}
}
