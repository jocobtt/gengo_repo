package main 

import "fmt"

func main() {
	var num1 int = 100
	var num2 int = 200 
	var str1 string = "poop"

	var ptr1 *int = &num1
	//var ptr1 *int = &str1 //compile error 

	fmt.Printf("mem address of num1 is %p\n", &num1)
	fmt.Printf("mem address of num2 is %p\n", &num2)
	fmt.Printf("mem address of str1 is %p\n", &str1)

	fmt.Printf("ptr1 points to mem address %p\n", ptr1)

	*ptr1 = 101
	fmt.Println(num1)
	
	ptr1 = &num2
	fmt.Printf("ptr1 points to mem address %p\n", ptr1)
	fmt.Print(*ptr1)
	
	ptr2 := new(int)
	ptr2 = ptr1
	fmt.Println(*ptr2)
}


