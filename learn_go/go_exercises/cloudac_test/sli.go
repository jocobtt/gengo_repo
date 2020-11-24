package main 

// slices build on main capabilites of arrays except slices are resizeable!!

import (
	"fmt"
)

func main() {
	arr1 := [6]int{1, 3, 5, 7, 11, 13}
	slice1 := []int{1, 3, 5, 7, 11, 13} // don't need to include size for the slice
	slice2 := slice[1:2]
	var slice3 = make([]int, 2, 3) // making slice of type integer, length of slice being 2 & capacity of slice being 3

	fmt.Println(arr1)
	fmt.Println(slice1)
	fmt.Println(slice2)
	fmt.Println(slice3)

	slice3 = slice1[1:4] // resizing slice3 by taking slice of slice 1

	fmt.Println(slice3)
	fmt.Println(len(slice3))

	slice1 = append(slice1, 200, 300, 400) // adding addtional elements to slice 1
	fmt.Println(slice)

	slice2 = append(slice2, []int{7, 8, 9}...) // ... = unpairing the slices
	fmt.Println(slice2)

	copyslice := make([]int, len(slice1))
	copy(copyslice, slice1)
	fmt.Println(copyslice)
}
// more likely to see slices in go source code