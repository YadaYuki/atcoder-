package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
	"strconv"
	"strings"
)

/*
 * Complete the 'minTime' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY processorTime
 *  2. INTEGER_ARRAY taskTime
 */

func minTime(processorTime []int32, taskTime []int32) int32 {
	processorTimeInt := make([]int, len(processorTime))
	taskTimeInt := make([]int, len(taskTime))
	for i := 0; i < len(processorTime); i++ {
		processorTimeInt[i] = int(processorTime[i])
	}
	for i := 0; i < len(taskTimeInt); i++ {
		taskTimeInt[i] = int(taskTime[i])
	}
	sort.Ints(processorTimeInt)
	sort.Ints(taskTimeInt)
	return processorTime[0] + taskTime[len(taskTime)-1]
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	processorTimeCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var processorTime []int32

	for i := 0; i < int(processorTimeCount); i++ {
		processorTimeItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		processorTimeItem := int32(processorTimeItemTemp)
		processorTime = append(processorTime, processorTimeItem)
	}

	taskTimeCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var taskTime []int32

	for i := 0; i < int(taskTimeCount); i++ {
		taskTimeItemTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
		checkError(err)
		taskTimeItem := int32(taskTimeItemTemp)
		taskTime = append(taskTime, taskTimeItem)
	}

	result := minTime(processorTime, taskTime)

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
