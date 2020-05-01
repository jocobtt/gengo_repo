package main 

import (
	"fmt"
)

func sum(num1 int, num2 int) int {
	result := num1 + num2
	return result
}

func minus(num1 int, num2 int) (result int) {
	result = num1 - num2
	return
}

func main() {
	fmt.Println(sum(1, 2))
	fmt.Println(minus(10,2))
	
	result := func(num1 int, num2 int) int {
		sum := sum(num1, num2)
		minus := minus(num1, num2)
		return sum * minus
	}(5, 3)

	fmt.Println(result)
}
