package main 

import (
	"flag"
	"fmt"
	"log"
	"math/rand"
	"os"
	"runtime/pprof"
	"time"
	
	G "gorgonia.org/gorgonia"
	"gorgonia.org/tensor"
)

const (
	// N = number of rows in dataset 
	N = 26733
	// feats is the number of features (x) in our dataset 
	feats = 10 
	// trainIter is the number iterations for which to train 
	trainIter = 500
)

var cpuprofile = flag.String("cpuprofile", "", "write cpu to file")
var memprofile = flag.String("memprofile", "", "write mem profile to file")
var static = flag.Bool("static", false, "Use static test file")
var wT tensor.Tensor 
var yT tensor.Tensor
var xT tensor.Tensor

// Float is an alias; in this ex we will generate random float64 values 
var Float = tensor.Float64 

// init generates random values for x, w, and y for test
// use static flag to load our own data 
// https://github.com/gorgonia/gorgonia/blob/master/examples/logisticregression/main.go
