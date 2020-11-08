package main 

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"

	"gonum.org/v1/gonum/stat"
)

func main() {
	// open the csv file 
	//f, err := os.Open("test.csv")
	//if err!= nil {
	//	log.Fatal(err)
	//}
	//defer f.Close()
	
	// create data values that are float64 format
	xs := []float64{
		32.32, 56.98, 21.52, 44.32, 
		55.63, 13.75, 43.47, 43.34,
		12.34,
	}

	fmt.Printf("data: %v\n", xs)

	// computes the weighted mean of the dataset 
	// weight is 1 - nil slice 
	mean := stat.Mean(xs, nil)
	variance := stat.Variance(xs, nil)
	stddev := math.Sqrt(variance)

	// stat.Quantile needs the input slice to be sorted 
	sort.Float(xs)
	fmt.Printf("data: %v (sorted\n", xs)

	// computes median of the dataset. 
	median := stat.Quantile(0.5, stat.Empirical, xs, nil)
	
	fmt.Printf("mean=      %v\n", mean)
	fmt.Printf("median=    %v\n", median)
	fmt.Printf("variance = %v\n", variance)
	fmt.Printf("std-dev= %v\n", stddev)
}
