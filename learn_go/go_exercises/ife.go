package main

import (
	"fmt"
)

func main() {
	var pop int = 400
	
	if pop < 350 {
		fmt.Println("small")
	} else if pop >= 350 && pop < 600 {
		fmt.Println("medium")
	} else {
		fmt.Println("large")
	}

	if toggle := true; toggle {
		fmt.Println("its on!")
	}
} 
