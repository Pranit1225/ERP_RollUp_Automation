import time 
import pyautogui
import pyperclip

#Disable PyAutoGui's Built-in Pause. We Define the Action Delay now as the single source
#pyautogui.PAUSE = 0

def run_automation(parts,delay, action_delay,  on_countdown, on_progress, on_complete,on_stopped, stop_event):

    total = len(parts)
    processed = 0
    part = ""

    try:

#! Countdown
    
        for seconds in range(delay, 0, -1):

            if stop_event.is_set():
                on_stopped(processed)
                return
            on_countdown(seconds)
            time.sleep(1)

#! Process Records

    
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
            time.sleep(action_delay)

            pyautogui.press("enter")

            #Record Successfully sent
            processed = current

            #Inform GUI of progress
            on_progress(current, total, part) 
        on_complete(total, part)

#? FAIL SAFE
    except pyautogui.FailSafeException:
        on_stopped(processed, "Fail-Safe Activated")   
        return

    except Exception as e:
        on_stopped(processed, f"Automation Error: {e}")
        return

    

                