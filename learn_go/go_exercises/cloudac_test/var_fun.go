package main 

import (
	"fmt"
)

func displayCount(id int, letters ...string) {
	count := 0
	for range letters {
		count++
	}

	// display id, letters count, letters type, and letters content
	fmt.Printf("%d - %d - %T - %s\n", id, count, letters, letters)
}

func main() {
	displayCount(1, "j", "a", "c", "o", "b")
	displayCount(2, "B", "r", "a", "s", "w", "e", "l", "l")

	cloud := []string{"s", "t", "u", "d"}
	displayCount(3, cloud...)
}
