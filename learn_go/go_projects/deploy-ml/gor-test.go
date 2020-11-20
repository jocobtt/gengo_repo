package main

import (
	"fmt"
	"log"

	. "gorgonia.org/gorgonia"

)

func main() {
	g := NewGraph()

	var x, y, z *Node
	var err error 

	// define the expression
	x = NewScalar(g, Float64, WithName("x"))
	y = NewScalar(g, Float64, WithName("y"))
	if z, err = Add(x, y); err != nil {
		log.Fatal(err)
	}
	
	// create a vm to run program on 
	machine := NewTapeMachine(g)
	defer machine.Close()

	//set initial values then run 
	Let(x, 2.0)
	Let(y, 2.5)
	if err = machine.RunAll(); err != nil {
		log.Fatal(err)
	}
	
	fmt.Printf("%v", z.Value())
}


