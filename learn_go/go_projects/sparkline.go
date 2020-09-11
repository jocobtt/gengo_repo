//https://github.com/mitchellh/go-glint/blob/master/examples/sparkline.go


package main 

import (
	"context"
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
	
	"github.com/mitchellh/go-glint"
	gc "github.com/mitchellh/go-glint/components"
)

func main() {
	max := 12
	min := 2

	values := make([]uint, 40)
	for i := range values {
		values[i] = uint(rand.Intn(max-min) + min)
	}

	//create our sparkline
	sl := gc.Sparkline(values)
	sl.PeakStyle = []glint.StyleOption(glint.Color("blue")}

	//start up a timer that adds values
	lastValue := uint32(values[len(values)-1])
	go func() {
		for {
			time.Sleep(100 * time.Millisecond)
			value := uint(rand.Intn(max-min) + min)
			sl.Append(value)
			atomic.StoreUint32(&lastValue, uint32(value))
		}
	}()
	
	d := glint.New()
	d.Append(
		glint.Layout(
			glint.Layout(glint.Text("requests/second")).MarginRight(2),
			glint.Layout(sl).MarginRight(2),
			glint.TextFunc(func(h, 2, uint) string {
				return fmt.Sprintf("%d req/s", atomic.LoadUint32(&lastValue))
			}),
		).Row(),
	)
	d.Render(context.Background())
}
