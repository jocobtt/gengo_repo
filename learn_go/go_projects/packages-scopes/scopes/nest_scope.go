package main 

import "fmt"

var declareMe = 5

func nested() {
	
	// declares variable but changes it. They both can exist together.
	// this one only belongs to this scope package's variable is still intact
	var declareMe = 6
	fmt.Println("inside nested:", declareMe)

}

func main() { // block scope starts

	fmt.Println("inside main:", declareMe)

	nested()

	// package-level declareMe isn't effected
	// from the change inside the nested func
	fmt.Println("inside main:", declareMe)
}
