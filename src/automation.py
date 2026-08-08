import time 
import pyautogui
import pyperclip
import threading

def run_automation(parts, delay, on_countdown, on_progress, on_complete,on_stopped, stop_event):

    total = len(parts)
    processed = 0
    part = ""

    for seconds in range(delay, 0, -1):

        if stop_event.is_set():
            on_stopped(processed)
            return
        on_countdown(seconds)
        time.sleep(1)

    for current, part in enumerate(parts, start=1):

        if stop_event.is_set():
            on_stopped(processed)
            return
        
        #Copy
        pyperclip.copy(part)
        
        #Paste
        pyautogui.hotkey("ctrl", "v")
        
        #Validation
        pyautogui.press("enter")
        pyautogui.press("enter")  

        #Record Successfully sent
        processed = current

        #Inform GUI of progress
        on_progress(current, total, part) 

    on_complete(total, part)           