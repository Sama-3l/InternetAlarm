import urllib.request
import winsound
import time
import pyautogui
import win32api

def hot_key_press():
     if win32api.GetKeyState(0x4D) < 0 and win32api.GetKeyState(0x4B) < 0 and win32api.GetKeyState(0x43)<0:
          return True

def check_connection(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return False
    except:
        return True
    
t = check_connection()
sec = 0

while t:
    sec = sec + 1
    time.sleep(1)
    t = check_connection()
    if sec % 60 == 0:
         pyautogui.hotkey('d')
         print(f"${sec} passed")

    if sec % 3600 == 0:
         print(f"Fuck Siva selvan. {sec} seconds passed")

    if t == False:
            for i in range(500):
                winsound.Beep(750, 800)
                time.sleep(0.3)
                if hot_key_press():
                    break