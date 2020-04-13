package main 

import (
	"fmt"
)

func main() {
	var isBig bool // defaults to false
	var isFast, hasFourWheels bool = false, true

	fmt.Println(isBig)
	fmt.Println(isFast)
	fmt.Println(hasFourWheels)

	fmt.Println(!hasFourWheels)
	fmt.Println(isFast && hasFourWheels)
	fmt.Println(isFast || hasFourWheels)

	if !isFast {
		fmt.Println("its slow!")
	}
	
	if hasFourWheels {
		fmt.Println("its a car!")
	}
	
}
