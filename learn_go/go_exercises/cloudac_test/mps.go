package main
// map is a collection of key value pairs that functions much like a dictionary
// maps are typed at comppile time and you can't mix and match types after a map has been declared
import (
	"fmt"
)
// 8-11 is a custom struct we create for line 30 w/ id being type int and rank being type int
type player struct {
	id int
	rank int
}

func main() {

	map1 := make(map[string]string)
	map1["key1"] = "value1"
	map1["key2"] = "value2"
	map1["key3"] = "value3"
	fmt.Println(map1)

	value1 := map1["key1"]
	fmt.Println(value1)

	//map1["key1"] = 10 //compile error
	map1["key1"] = "value1.1"
	delete(map1, "key2")
	map1["newkey"] = "value4"
	fmt.Println(map1)

	team := map[string]player{"john": {3, 10}, "bob": {14, 11}}

	fmt.Println(team)


}