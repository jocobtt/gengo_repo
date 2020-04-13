package main 
import (
	"fmt"
)

func main() {
	var count1 int 
	var count2 int = 100 
	count3 := 200 
	count4 := count2 + count3

	fmt.Println("count1 is:" , count1, ". since we haven't assigned anything to it yet") // prints 0 
	count1 = 10
	fmt.Println(count1, "count1 is now 10 since we have assigned that value to it") // prints 10 

	fmt.Println(count2)
	fmt.Println(count3)
	fmt.Println(count4)

	count3++ // increment integer variables
	count4-- // decrement integer variable 

	fmt.Println("print count3 and then count4 after we have incremented it")
	fmt.Println("count3 is: ", count3,"count4 is: ", count4)

	fmt.Println("count3 * count4 is: ", count3 * count4) // multiply count3 and count4
}
