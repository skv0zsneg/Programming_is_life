/*
Определите является ли билет счастливым. Счастливым считается билет, в
шестизначном номере которого сумма первых трёх цифр совпадает с суммой трёх последних.

Формат входных данных

На вход подается номер билета - одно шестизначное  число.

Формат выходных данных
Выведите "YES", если билет счастливый, в противном случае - "NO".

Sample Input:
613244

Sample Output:
YES
*/

package main

import "fmt"

func main() {
	var number int
	var sum_first int
	var sum_second int

	fmt.Scan(&number)
	sum_first = number%10 + (number%100)/10 + (number%1000)/100
	sum_second = (number%10000)/1000 + (number%100000)/10000 + (number%1000000)/100000
	fmt.Print(sum_first, sum_second)
	if sum_first == sum_second {
		fmt.Print("YES")
	} else {
		fmt.Print("NO")
	}
}
