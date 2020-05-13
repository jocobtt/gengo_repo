package main

import "fmt"

type person struct {
	firstname string
	lastname  string
	age       int 
	height    float64
}

func (p *person) fullname() string {
	return p.firstname + " " + p.surname
}

func (p *person) canDrive() bool {
	if p.age >=20 {
		return true
	} else if p.height > 5.5 { 
		return true 
	}
	else {
		return false 
	}
}

func (p *person) updateAge(newAge int) {
	p.age = newAge 
}

func main() {
	person1 := person{"Frank", "Centura", 40, 5.11} 
	person2 := person{"John", "Dear", 18, 5.4}

	fmt.Printf("%s can drive: %t\n", person1.fullname(), person1.canDrive())
	fmt.Printf("%s can drive: %t\n", person2.fullname(), person2.canDrive())

	person2.updateAge(person2.age + 1) // Johns birhtday 
	fmt.Println(person2.age)

	fmt.Printf("%s can drive: %t\n", person2.fullname(), person2.canDrive())
}
