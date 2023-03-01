import argparse
import json
from time import sleep
import datetime
import pyautogui
from function import Function

def start():

	Function.locateClick('resources/event/play.png')

	bonus = pyautogui.locateCenterOnScreen('resources/event/bonus.png',confidence=0.9)
	while bonus == None:
		sleep(0.5)
		right = pyautogui.locateCenterOnScreen('resources/map/right.png',confidence=0.9)
		pyautogui.click(right.x, right.y)
		sleep(0.5)
		bonus = pyautogui.locateCenterOnScreen('resources/event/bonus.png',confidence=0.9)
	pyautogui.click(bonus.x, bonus.y)
	sleep(0.5)
	
	Function.locateClick('resources/difficulty/easy.png')

	Function.locateClick('resources/difficulty/play.png')
	
start()






# print(pyautogui.locateCenterOnScreen('resources/difficulty/easy.png', confidence=0.9))
