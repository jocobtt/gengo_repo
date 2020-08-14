package main

// file scope
import "fmt"

// package scope 
const ok = "some string here"

func main() {
	var hello = "hello"

	fmt.Println(hello, ok)
}