package main

import (
    "fmt"
    "net"
    "os"
    "strconv"
    "time"
    "math/rand"
    "strings"
)

const (
    FLAG = "A Fla⚡️H in the night❗"
    MAX_DEPTH = 1024
)

var taken_ports = []int {31337}
var letters = []rune("abcdefABCDEF0123456789")
var min_port = 10000
var max_port = 65535

func init() {
    rand.Seed(time.Now().UnixNano())
}

func contains(haystack []int, needle int) bool {
    for _, v := range haystack {
        if v == needle {
            return true
        }
    }
    return false
}


func randSeq(n int) string {
    b := make([]rune, n)
    for i := range b {
        b[i] = letters[rand.Intn(len(letters))]
    }
    return string(b)
}

type PortConfig struct {
    secret string
    port  int
    depth int
    time int64
}


func next_config(depth int) PortConfig{
    var next_port = -1
    for {
        next_port = rand.Intn(max_port - min_port) + min_port
        if !contains(taken_ports, next_port) {
            taken_ports = append(taken_ports, next_port)
            break
        }
    }
    return PortConfig{secret: randSeq(32), port: next_port, depth: depth + 1, time: time.Now().UnixMilli()}
}

func listen(config PortConfig) {
    // fmt.Println("Server Running...")
    server, err := net.Listen("tcp", "localhost:"+strconv.Itoa(config.port))
    if err != nil {
        fmt.Println("Error listening:", err.Error())
        os.Exit(1)
    }
    defer server.Close()
    // fmt.Println("Listening on localhost:" + strconv.Itoa(config.port))
    // fmt.Println("Waiting for client...")
    for {
        connection, err := server.Accept()
        if err != nil {
                fmt.Println("Error accepting: ", err.Error())
                os.Exit(1)
        }
        // fmt.Println("client connected")
        if config.depth != -1 && time.Now().UnixMilli() - config.time > 1000 {
            buffer := make([]byte, 1024)
            _, err := connection.Read(buffer)
            if err != nil {
                fmt.Println("Error reading:", err.Error())
            }
            _, err = connection.Write([]byte(fmt.Sprintf("You are %d ms late\n", time.Now().UnixMilli() - config.time - 1000)))
            connection.Close()
            break
        } else {
            go processClient(connection, config)
        }
    }
}

func processClient(connection net.Conn, config PortConfig) {
    buffer := make([]byte, 1024)
    mLen, err := connection.Read(buffer)
    if err != nil {
        fmt.Println("Error reading:", err.Error())
    }
    received := strings.TrimSpace(string(buffer[:mLen]))
    if len(config.secret) == 0 || config.secret == received {
        if config.depth == MAX_DEPTH {
            _, err = connection.Write([]byte(fmt.Sprintf("You made it in time! %s\n", FLAG)))
            os.Exit(0)
        } else if config.depth == -1 {
            new_config := next_config(config.depth)
            _, err = connection.Write([]byte(fmt.Sprintf("We are out of time! Quickly send %s to port %d\n", new_config.secret, new_config.port)))
            go listen(new_config)
        } else {
            new_config := next_config(config.depth)
            _, err = connection.Write([]byte(fmt.Sprintf("Great, you are just in time! Quickly send %s to port %d\n", new_config.secret, new_config.port)))
            go listen(new_config)
        }
    } else {
        _, err = connection.Write([]byte("What's that?!"))
    }
        connection.Close()
}

func main() {
    listen(PortConfig{secret: "", port: 31337, depth: -1, time: time.Now().UnixMilli()})
}