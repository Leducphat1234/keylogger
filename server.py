def main():
    import socket
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 4000
    FORMAT = "utf-8"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            HOSTNAMECLIENT = conn.recv(64).decode()
            print("$Connection accepted$")
            print(HOSTNAMECLIENT)
            while True:
                try:
                    data = conn.recv(64).decode(FORMAT)
                    print(data)
                except ConnectionResetError:
                    break

if __name__ == "__main__":
    main()