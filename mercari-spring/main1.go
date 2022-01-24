package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'updateTimes' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY signalOne
 *  2. INTEGER_ARRAY signalTwo
 */

func updateTimes(signalOne []int32, signalTwo []int32) int32 {
	// Write your code here
	var maxSignal int32
	maxSignal = 0
	n := len(signalOne)
	m := len(signalTwo)
	minVal := 0
	if n > m {
		minVal = m
	} else {
		minVal = n
	}
	ans := 0
	for i := 0; i < minVal; i++ {
		if signalOne[i] == signalTwo[i] && maxSignal < signalOne[i] {
			maxSignal = signalOne[i]
			ans += 1
		}
	}
	return int32(ans)
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	signalOneCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var signalOne []int32

	for i := 0; i < int(signalOneCount); i++ {
		signalOneItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		signalOneItem := int32(signalOneItemTemp)
		signalOne = append(signalOne, signalOneItem)
	}

	signalTwoCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var signalTwo []int32

	for i := 0; i < int(signalTwoCount); i++ {
		signalTwoItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		signalTwoItem := int32(signalTwoItemTemp)
		signalTwo = append(signalTwo, signalTwoItem)
	}

	result := updateTimes(signalOne, signalTwo)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
