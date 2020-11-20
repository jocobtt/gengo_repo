package main

import (
	"fmt"
)

type person struct {
	firstname string
	surname   string
}

type lecture struct {
	name       string
	instructor person
	duration   int //seconds
}

func main() {
	lectures := []lecture{
		lecture{"structs", person{"jacob", "braswell"}, 300},
		lecture{"pointers", person{"jacob", "braswell"}, 300},
		lecture{"functions", person{"jacob", "braswell"}, 300},
	}

	for _, lecture := range lectures {
		name := lecture.name
		instructor := fmt.Sprintf("%s %s", 
			lecture.instructor.firstname,
			lecture.instructor.surname)
		duration := lecture.duration

		fmt.Printf("lecture: '%s', AuthorL %s, Duration %d secs\n", name, instructor, duration)
	}
}
