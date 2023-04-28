package main 
// https://github.com/fyne-io/examples/
import (
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	a := app.New()
	w := a.NewWindow("Test, Hello")

	hello := widget.NewLabel("Hello You!")
	w.SetContent(container.NewVBox(
		hello,
		widget.NewButton("Hi!", func() {
			hello.SetText("welcome :)")
		}),
	))

	w.ShowAndRun()
}