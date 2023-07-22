from string import ascii_letters,digits
import random
import time
import threading
import socket

NET_HOST="signal.vsfi.org"
NET_PORT=8745
NOISE_CHARS=ascii_letters.join(digits)

def spam(client):
    try :
        while True:
            client.send(NOISE_CHARS[random.randrange(0, len(NOISE_CHARS))].encode())
            time.sleep(0.01)
    except BrokenPipeError as e:
        return

def qr(client):
    try:
        while True:
            with open('answer.txt', 'r') as file:
                data = file.read().replace('\n', '$')
                for i in range(len(data)):
                    time.sleep(random.uniform(0.01, 0.1))
                    client.send(data[i].encode())
                client.send('&'.encode())
    except BrokenPipeError as e:
        return


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((NET_HOST, NET_PORT))
sock.listen()

while (True):
    (clientConnected, clientAddress) = sock.accept()

    spamThread = threading.Thread(target=spam, args=(clientConnected,), daemon=False)
    spamThread.start()

    qrThread = threading.Thread(target=qr, args=(clientConnected,), daemon=False)
    qrThread.start()


