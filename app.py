import urllib.request
import winsound
import time
import pyautogui

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