package main 

import (
	"fmt"
	"strings"
)

type upstring string

func (msg upstring) up() string {
	s := string(msg)
	return strings.ToUpper(s)
}

func main() {
	message := upstring("hello, boss")
	fmt.Println(message.up())
}
