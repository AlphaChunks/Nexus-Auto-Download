import pyautogui
import time
import os
import keyboard

scriptDir = os.path.dirname(os.path.abspath(__file__))
targetPath = os.path.join(scriptDir, "nexus.png") # filename for scan

print("Scanning, press # to stop.")

try:
    while True:
        if keyboard.is_pressed('#'): # key to exit
            print("Exit has been pressed, ending script.")
            break

        location = pyautogui.locateOnScreen(target_path, confidence=0.8)

        if location:
            center = pyautogui.center(location)
            pyautogui.moveTo(center.x, center.y, duration=0.2)
            pyautogui.click()
            print(f"Clicked @: {center}")

        time.sleep(0.25)

except keyboardInterrupt:
    print("Ended.")
