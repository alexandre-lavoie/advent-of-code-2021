package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func load_input(path string) ([]int, error) {
	bytes, err := os.ReadFile(path)

	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(bytes), "\n")
	positions := make([]int, len(lines))

	for index, line := range lines {
		tokens := strings.Split(line, " ")
		position := tokens[len(tokens)-1]
		positions[index], err = strconv.Atoi(position)

		if err != nil {
			return nil, err
		}

		positions[index] -= 1
	}

	return positions, nil
}

func task1(path string) (int, error) {
	positions, err := load_input("../input.txt")

	if err != nil {
		return -1, err
	}

	scores := make([]int, len(positions))
	playing := 0
	var i int

	for i = 0; true; i += 3 {
		done := false
		offset := 0

		for j := i; j < i+3; j++ {
			offset += (j % 100) + 1
		}

		positions[playing] = (positions[playing] + offset) % 10
		scores[playing] += positions[playing] + 1

		if scores[playing] >= 1000 {
			done = true
		}

		playing = (playing + 1) % len(positions)

		if done {
			break
		}
	}

	i += 3

	return i * scores[playing], nil
}

func tasks(path string) error {
	t1, err := task1(path)

	if err != nil {
		return err
	}

	fmt.Println("Task 1:", t1)

	// I am not even trying task 2 in this.

	return nil
}

func main() {
	path := "input.txt"
	err := tasks(path)

	if err != nil {
		panic(err)
	}
}
