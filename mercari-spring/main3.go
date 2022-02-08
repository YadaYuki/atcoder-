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
 * Complete the 'countSentences' function below.
 *
 * The function is expected to return a LONG_INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY wordSet
 *  2. STRING_ARRAY sentences
 */

func countSentences(wordSet []string, sentences []string) []int64 {
	// Write your code here
	// count anagrams
	anagramCountMap := make(map[string]int)
	for _, word := range wordSet {
		s := strings.Split(word, "")
		sort.Strings(s)
		str := strings.Join(s, "")
		anagramCountMap[str]++
	}
	ansLs := make([]int64, 0)
	for _, sentence := range sentences {
		wordsInSentence := strings.Split(sentence, " ")
		ans := 1
		for _, word := range wordsInSentence {
			s := strings.Split(word, "")
			sort.Strings(s)
			sortedWord := strings.Join(s, "")

			ans = anagramCountMap[sortedWord] * ans
		}
		ansLs = append(ansLs, int64(ans))
	}
	return ansLs
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	wordSetCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var wordSet []string

	for i := 0; i < int(wordSetCount); i++ {
		wordSetItem := readLine(reader)
		wordSet = append(wordSet, wordSetItem)
	}

	sentencesCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)

	var sentences []string

	for i := 0; i < int(sentencesCount); i++ {
		sentencesItem := readLine(reader)
		sentences = append(sentences, sentencesItem)
	}

	result := countSentences(wordSet, sentences)

	for i, resultItem := range result {
		fmt.Fprintf(writer, "%d", resultItem)

		if i != len(result)-1 {
			fmt.Fprintf(writer, "\n")
		}
	}

	fmt.Fprintf(writer, "\n")

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
