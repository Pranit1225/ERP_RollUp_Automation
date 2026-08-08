import time 
import pyautogui
import pyperclip
import threading

def run_automation(parts, delay, on_countdown, on_progress, on_complete):

    total = len(parts)

    for seconds in range(delay, 0, -1):
        on_countdown(seconds)
        time.sleep(1)

    for current, part in enumerate(parts, start=1):
        
        #Copy
        pyperclip.copy(part)
        
        #Paste
        pyautogui.hotkey("ctrl", "v")
        
        #Validation
        pyautogui.press("enter")
        pyautogui.press("enter")  

        #Inform GUI of progress
        on_progress(current, total, part) 

    on_complete(total, part)           