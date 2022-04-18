/* const (
	c0 = iota  // c0 == 0
	c1 = iota  // c1 == 1
	c2 = iota  // c2 == 2
  )
  fmt.Println(c0, c1, c2) // вывод: 0 1 2
  
  
  const (
	  Sunday = iota
	  Monday
	  Tuesday
	  Wednesday
	  Thursday
	  Friday
	  Saturday
	  _  // пропускаем 7
	  Add
  )
  
  fmt.Println(Sunday)   // вывод: 0
  fmt.Println(Saturday) // вывод: 6
  fmt.Println(Add) // вывод: 8
  
  
  
  const (
	  u         = iota * 42 // u == 0 (индекс - 0, поэтому 0 * 42 = 0)
	  v float64 = iota * 42 // v == 42.0 (индекс - 1, поэтому 1.0 * 42 = 42.0)
	  w         = iota * 42 // w == 84  (индекс - 2, поэтому 2 * 42 = 84)
  )
  
  // переменные ни в одном блоке const, поэтому индекс не увеличился
  const x = iota  // x == 0
  const y = iota  // y == 0
  */
package main

import "fmt"

const (
	Sunday = iota
	Monday
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	_  // пропускаем 7
	Add
)

func main() {
	fmt.Println(Sunday, Monday, Add) // 0 1 8
}
