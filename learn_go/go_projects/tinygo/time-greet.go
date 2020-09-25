package main 

import (
	"fmt"
	"time"
)

func main() {
	greet()
	eat()
}

func greet() {
	h := time.Now().Hour()
	switch {
	case h >= 4 && h <= 9:
		fmt.Println("おはようさん！")
	case h >= 10 && h <= 16:
		fmt.Println("こんにちは！")
	default: 
		fmt.Println("こんばんは！")
	}
}

func eat() {
	e := time.Now().Hour()
	switch {
	case e >= 7 && <= 10:
		fmt.Println("朝食の時間だよ！")
	case e >= 11 && <= 1:
		fmt.Println("昼ご飯の時間ですよ！")
	case e >= 14 && <= 19:
		fmt.Println("夕食の時間だよ！")
	default:
		fmt.Println("まだご飯を食べる時間じゃないよ！食べ過ぎたら太っちゃうよ！")
	}
}
