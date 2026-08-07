import time 
import pyautogui
import pyperclip

def run_automation(parts, delay):

    time.sleep(delay)

    for part in parts:

        #Copy
        pyperclip.copy(part)

        #Paste
        pyautogui.hotkey("ctrl", "v")

        #Validation
        pyautogui.press("enter")
        pyautogui.press("enter")