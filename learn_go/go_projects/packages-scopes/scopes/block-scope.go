package main

func nope() {
	const ok = "test"
	var hello = "hello"
	
	_ = hello
}

func main() {
	// above stuff isn't visable here

	//ERROR:
	// fmt.Println(hello, ok)

} 
