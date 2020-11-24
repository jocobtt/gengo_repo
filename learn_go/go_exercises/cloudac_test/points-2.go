package main

import "fmt"

func notString(msg string) {
	msg = fmt.Sprintf("not%s", msg)
}

func notStringPtr(msg *string) {
	*msg = fmt.Sprintf("not%s", *msg)
}

func main() {
	message := "Jacob is poopy"

	notString(message)
	fmt.Println(message)

	notStringptr(message)
	fmt.Println(message)
}
