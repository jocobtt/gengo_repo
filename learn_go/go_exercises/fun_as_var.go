package main

import (
	"fmt"
)

func extend(val string) func() string {
	i := 0
	return func() string {
		i++ 
		return val[:i]
	}
}

func main() {
	ja := "Jacob"
	
	word := extend(ja)
	
	for i := 0; i < len(ja); i++ {
		fmt.Println(word())
	}
}
