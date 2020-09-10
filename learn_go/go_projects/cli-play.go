package main 

import (
	"os"
	"fmt"
	"log"
	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{
		Name: "greet",
		Usage: "Make sure to social distance",
		Action: func(c *cli.Context) error {
			fmt.Println("Dude! What's up?")
			retrun nil
		},
	}

	err := app.Run(os.Args)
	if err != nil {
		log.Fatal(err)
	}
}