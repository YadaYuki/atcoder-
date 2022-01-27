package main

import (
	"fmt"
	"sort"
	"strings"
)

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
	wordSet := []string{
		"the",
		"bats",
		"tabs",
		"in",
		"cat",
		"act",
	}
	sentences := []string{
		"cat the bats",
		"in the act",
		"act tabs in",
	}
	fmt.Println(countSentences(wordSet, sentences))
}
