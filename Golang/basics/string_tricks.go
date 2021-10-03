package main

import "fmt"

func main() {
	fmt.Println("Hi, Go!ы")
	// Строка - это набор символов. Символы - это байты. Обращение по индексу будет к байту.
	fmt.Println("Hi, Go!ы"[7]) // 209

	// Для обращения к символу нужно преобрзоваьт байт в строку.
	fmt.Println(string("Hi, Go!ы"[7])) // Ñ
}
