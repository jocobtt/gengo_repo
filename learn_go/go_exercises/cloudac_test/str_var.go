package main 

import (
	"fmt"
)

var (
	Name1 string = "global1"
	Name2 string = "global2"
)
// the above variables are considered global since they are declared outside of the function and names begin w/ capital letter

var var1, var2 string = "local1", "local2"

func main() {
	var name1 string 
	var name2 string = "Jacob"
	name3 := "DevOps iz lyfe"
	name4 := name2 + " " + name3

	// := is a shortened way of defining a variable 

	fmt.Println(name1)  // prints an empty string
	name1 = "blah"
	fmt.Println(name1) // prints Blah

	fmt.Println(name2)
	fmt.Println(name3)
	fmt.Println(name4)


	fmt.Printf("%v -- %v\n", name2, name3) // string formatters printf function

	fmt.Println(Name1, Name2, var1, var2)
}

