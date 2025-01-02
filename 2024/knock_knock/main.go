package main

import (
	"fmt"
	"log"
	"net"
	"net/http"
	"strings"
	"sync"
	"time"
)

const (
	customHeader        = "X-My-Shisha-Header"
	expectedHeaderValue = "Gopher"
	requiredAttempts    = 3
	timeoutDuration     = 10 * time.Minute
	basePort            = 6097
	divisor             = 58
)

type clientInfo struct {
	attempts int
	lastTime time.Time
}

var (
	clientAttempts = make(map[string]*clientInfo)
	mu             sync.Mutex
)

func main() {
	ports := [49]int{5745, 8385, 9523, 4384, 9641, 8476, 7200, 7987, 6712, 5475, 5794, 8640, 8803, 5295, 9355, 6886, 7023, 7440, 6354, 4261, 7086, 8715, 8153, 9085, 4295, 9212, 6606, 5034, 5375, 8309, 6376, 7362, 6634, 9367, 7834, 4712, 8908, 6434, 6792, 4250, 7670, 8952, 8430, 5690, 5315, 6709, 9229, 7098, 4518}

	log.Printf("Special port is: %d", basePort)
	go startSpecialServer(basePort)
	for _, port := range ports {
		go startKnockHeadServer(port)
	}

	go cleanupOldEntries()

	select {}
}

func startKnockHeadServer(port int) {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Knock yourself on the head"))
	})
	server := &http.Server{
		Addr:    fmt.Sprintf(":%d", port),
		Handler: mux,
	}
	log.Printf("Starting knock head server on :%d", port)
	log.Fatal(server.ListenAndServe())
}

func startSpecialServer(port int) {
	mux := http.NewServeMux()
	mux.HandleFunc("/", handler)
	server := &http.Server{
		Addr:    fmt.Sprintf(":%d", port),
		Handler: mux,
	}
	log.Printf("Starting special server on :%d", port)
	log.Fatal(server.ListenAndServe())
}

func handler(w http.ResponseWriter, r *http.Request) {
	clientIP := getClientIP(r)
	headerValue := r.Header.Get(customHeader)

	log.Printf("Received request from %s with header %s: %s", clientIP, customHeader, headerValue)

	if headerValue == "" {
		http.Error(w, "Forbidden", http.StatusForbidden)
		return
	}

	mu.Lock()
	defer mu.Unlock()

	info, exists := clientAttempts[clientIP]
	if !exists {
		info = &clientInfo{attempts: 0, lastTime: time.Now()}
		clientAttempts[clientIP] = info
	}

	if time.Since(info.lastTime) > timeoutDuration {
		// Reset attempts if the last attempt was too long ago
		info.attempts = 0
		info.lastTime = time.Now()
	}

	if headerValue == expectedHeaderValue {
		info.attempts++
		info.lastTime = time.Now()
		if info.attempts >= requiredAttempts {
			w.Header().Set("X-Special-Response", "access-granted")
			w.Write([]byte("You've found Sir Gopher!\n"))
			// Reset attempts after successful access
			info.attempts = 0
		} else {
			w.Write([]byte(fmt.Sprintf("Attempt %d/%d\n", info.attempts, requiredAttempts)))
		}
	} else {
		http.Error(w, "Forbidden", http.StatusForbidden)
	}
}

func getClientIP(r *http.Request) string {
	xff := r.Header.Get("X-Forwarded-For")
	if xff != "" {
		ips := strings.Split(xff, ",")
		return strings.TrimSpace(ips[0])
	}
	ip, _, _ := net.SplitHostPort(r.RemoteAddr)
	return ip
}

func cleanupOldEntries() {
	for {
		time.Sleep(1 * time.Minute)
		mu.Lock()
		for ip, info := range clientAttempts {
			if time.Since(info.lastTime) > timeoutDuration {
				delete(clientAttempts, ip)
			}
		}
		mu.Unlock()
	}
}
