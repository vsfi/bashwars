package main

import (
  "fmt"
  "os"
)

func main() {
  pincode := os.Args[1]
  pingcode1 := 99887798274827643
  if pincode == "0787" {
    fmt.Printf("flag is %d\n",pingcode1)
  } else {
    fmt.Println("WRONG!")
  }
}