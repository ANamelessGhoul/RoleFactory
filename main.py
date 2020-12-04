import pyautogui
import time
import pyperclip

file = open("people.txt", "r",  encoding="utf-8")
fileLines = file.readlines()
line_count = len(fileLines)

start_delay = 10
wait_time = 10

for i in range(0,start_delay + 1):
    print("Time to start: " + str(start_delay - i))
    time.sleep(1)

for line in fileLines:
    print("Lines Remaining: " + str(line_count))
    line_count -= 1
    pyperclip.copy(f'?temprole @{line[:-1]} 12h Atölye 2 Katılımcısı')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(wait_time)