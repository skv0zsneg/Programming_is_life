/*
Напишите программу, которая в последовательности чисел находит сумму 
двузначных чисел, кратных 8. Программа в первой строке получает на вход число 
n - количество чисел в последовательности, во второй строке -- n чисел, 
входящих в данную последовательность.

Sample Input:
5
38 24 800 8 16

Sample Output:
40
*/

package main

import "fmt"

func main() {
	var seq int
	var another int
	var sum int = 0

	fmt.Scan(&seq)

	for i := 0; i < seq; i++{
		fmt.Scan(&another)
		if 9 < another && another < 100 && another % 8 == 0 {
			sum += another
		} 
	}

	fmt.Println(sum)
}