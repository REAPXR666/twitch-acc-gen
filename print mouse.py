import pyautogui
import keyboard
import random
import time

delay = int(input("How long to wait till it prints your mouse: "))

time.sleep(delay)
print(pyautogui.position())
pos = pyautogui.position()
f = open("MouseLocation.txt", "w")
f.write("LATEST POINT: \n")
f.write(str(pos))
f.write("\n")
f.close()
