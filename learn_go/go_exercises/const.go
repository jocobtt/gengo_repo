package main 

import (
	"fmt"
)

// const maxValue // compile error 

const popu int = 1000

func main() {
	const name = "Jabrazzy"

	// name = "blah" //compile error

	if true {
		const color = "red"
		
		fmt.Println(popu)
		fmt.Println(name)
	}
	
	//fmt.Println(color) //compile error
}
