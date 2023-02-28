import argparse
import json
from time import sleep
import datetime
import pyautogui


# class Point:
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
		
def move_mouse_to(point):
	pyautogui.moveTo(point.x, point.y)
	
def move_and_click_it(point):
	pyautogui.click(point.x, point.y)

def locateCenterOnScreen(img_location):
	location = pyautogui.locateCenterOnScreen(img_location)
	return (location.x, location.y) if location else "pika"
pyautogui.hotkey("alt","tab")
sleep(1)
print(pyautogui.locateCenterOnScreen('resources/event/play2.png', confidence=0.9))
print()
