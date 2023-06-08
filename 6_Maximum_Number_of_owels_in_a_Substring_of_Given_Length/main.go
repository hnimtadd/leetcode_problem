package main

import (
	"fmt"
)

// Given a string s and an integer k, return the maximum number of vowel lettes in any substring of s wich length k

func maxVowels(s string, k int) int {
	counter := 0
	res := 0
	for i := 0; i < len(s); i++ {
		if isVowel(s[i]) {
			counter++
		}
		if i >= k {
			if isVowel(s[i-k]) {
				counter--
			}
		}
		res = max(res, counter)
	}
	return res
}
func isVowel(char byte) bool {
	return char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u'
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// func spiralOrder(matrix [][]int) []int {
// 	var array []int
// 	helper(matrix, &array, 0, 0)
// 	return array
// }

//	func helper(matrix [][]int, array *[]int, i, j int) {
//		if i >= 0 && j >= 0 && i < len(matrix) && j < len(matrix[0]) && matrix[i][j] != -999999 {
//			*array = append(*array, matrix[i][j])
//			matrix[i][j] = -999999
//			if i == 0 || matrix[i-1][j] == -999999 {
//				helper(matrix, array, i, j+1)
//			}
//			helper(matrix, array, i+1, j)
//			helper(matrix, array, i, j-1)
//			helper(matrix, array, i-1, j)
//		}
//	}
func permutations(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{}
	} else {
		return helper(nums[1:], []int{nums[0]})
	}

}
func insert(a []int, index int, value int) []int {
	if len(a) == index { // nil or empty slice or after last element
		return append(a, value)
	}
	a = append(a[:index+1], a[index:]...) // index < len(a)
	a[index] = value
	return a
}
func helper(nums []int, cNum []int) [][]int {
	res := [][]int{}
	if len(nums) != 0 {
		curr := nums[0]
		nums = nums[1:]
		for i := 0; i <= len(cNum); i++ {
			tmp := insert(cNum, i, curr)
			n := helper(nums, tmp)
			res = append(res, n...)

		}
		return res
	}
	return [][]int{cNum}

}

// 00 01 02 12 22 21 20 10 11
// y tang, x tang, x giam, y giam
func main() {
	// s := "tryhard"
	// k := 4
	// fmt.Println(maxVowels(s, k))
	// matrix := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	// fmt.Print(spiralOrder(matrix))
	nums := []int{1, 2, 3}
	fmt.Println(permutations(nums))

}
