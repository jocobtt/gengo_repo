package main 

import (
	"fmt"
)

func main() {
	var arr1[4]int // int w/ 0s space of 4 integers
	arr2 := [...]int{3, 1, 5, 10, 100} //compiler infers size of array
	fmt.Println(arr1)
	fmt.Println(arr2)

	fmt.Println(len(arr1)) //4
	fmt.Println(len(arr2)) //5

	for _, value := range arr2 {
		fmt.Println(value) // iterate over an array using range. _ is how we recieve and discard the index value

	}

	arr1[0] = 10 //setting - how you index and update a value
	// arr1[4] = 1 // compile error - out of bounds. 

	fmt.Println(arr1)
	fmt.Println(arr1[0]) // getting 

	// multidimensional - an array of arrays
	arr3 := [2][2]string{
		{"a1", "a2"},
		{"b1", "b2"}, // trailing comma is mandatory
	}
	
	fmt.Println(arr3)
}
// arrays have a fixed size, you cannot re-arrange arrays. there is a slice data structure though. length is apart of its type 