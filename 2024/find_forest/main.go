package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"time"
)

func RandInt(lower, upper int) int {
	rand.Seed(time.Now().UnixNano())
	rng := upper - lower
	return rand.Intn(rng) + lower
}

func main() {
	ext := []string{".txt", ".est", ".blr", ".bgr", ".kzh", ".pol", ".srb", ".svk", ".svn", ".geo", ".fin"}
	fileNames := []string{"forest", "flower", "mushroom", "tree", "cone", "woodpecker", "belka", "duplo"}
	os.MkdirAll("/inventory/", os.ModePerm)
	currentTime := time.Now().Local()
	rand.Seed(time.Now().Unix())
	for range [500]int{} {
		randFilename := fileNames[rand.Int()%len(fileNames)] + "*" + ext[rand.Int()%len(ext)]
		f, err := os.CreateTemp("/inventory/", randFilename)
		if err != nil {
			log.Fatal(err)
		}
		newDate := currentTime.AddDate(RandInt(-5, 5), RandInt(-5, 5), RandInt(-5, 5))
		if _, err := f.Write([]byte("I'm sorry, but your hollow is in another castle.")); err != nil {
			log.Fatal(err)
		}
		if err := os.Chtimes(f.Name(), newDate, newDate); err != nil {
			fmt.Println(err)
		}
		if err := f.Close(); err != nil {
			log.Fatal(err)
		}
	}
	findFileName := "/inventory/forest05021997.fin"
	if err := os.WriteFile(findFileName, []byte("NICE HOLLOW\n"), 0600); err != nil {
		log.Fatal(err)
	}
	then := currentTime.AddDate(-1, -1, -1)
	if err := os.Chtimes(findFileName, then, then); err != nil {
		fmt.Println(err)
	}
}
