package main 

import (
	"fmt"
)

func main() {
	x:= 0
	y:= 0
	// add to x until it is up to 2
	for {
		if x++; x > 2 {
			fmt.Println(x)
			break
		}
	}
	// keep looping while y is less than 3
	for y < 3 {
		fmt.Println(y)
		y++ 
	}
	// sets z to 0, has test case and then adds one to z until it is at 8. continue means it will run the for loop w/o running remaining statements.
	for z := 0; z < 10; z++ { 
		if z < 8 {
			continue
		}
		fmt.Println(z)
	}
}
