package main
// range can be used to iterate over arrays, slices and maps
import (
	"fmt"
)

type player struct {
	id int
	rank int
}

func main() {
	bytes := []int{67, 108, 111, 117, 100, 65, 99, 97, 100, 101, 109, 121} // creating byte slice of type int
	for idx, value := range bytes {
		fmt.Print(string(value))
		if len(bytes)-1 == idx {
			fmt.Println()
		}
	} // iterating over the byte using range then convert each number to its character value 
	
	team := map[string]player{"Josh": {3, 10}, "Bob": {14, 11}}
	fmt.Println(team)

	for key, value := range team {
		fmt.Printf("%s -> %d\n", key, value)
	} // how to use range to iterate over a map
	
	for _, value := range team {
		fmt.Println(value)
	} // _ discards the key

	for key := range team {
		fmt.Println("key:", key)
	}
}
