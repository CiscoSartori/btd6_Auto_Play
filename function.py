import argparse
import json
from time import sleep
import datetime
import pyautogui
import pydirectinput






class Function:
	def locateClick(img):
		location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
		pyautogui.click(location.x, location.y)
		sleep(0.5)
	

	def map_verify(img):
		game_map = None
		array_map = 0
		while game_map == None:
			game_map = pyautogui.locateCenterOnScreen('resources/map/'+img[array_map]+'.png', confidence=0.9)
			array_map += 1
		array_map -= 1
		return array_map
	

	def round_verify(final, start):

		while start < final:
			screen = pyautogui.screenshot(region=(1466,31, 38, 34))
			round = pyautogui.locateCenterOnScreen(screen, confidence=0.9)
			while round != None:
				round = pyautogui.locateCenterOnScreen(screen, confidence=0.95)
			start += 1
			print('round',start)
			sleep(2)
		return start

	def place_tower(tower_type, location):
		pydirectinput.press(tower_type)
		sleep(0.1)
		pyautogui.moveTo(location[0], location[1])
		sleep(0.1)
		pyautogui.click(location[0], location[1])
		sleep(0.2)
	
	def upgrade_tower(up1,up2,up3,location):
		pyautogui.click(location[0], location[1])
		sleep(0.1)
		while up1 != 0:
			pydirectinput.press(',')
			up1-=1
			sleep(0.1)
		while up2 != 0:
			pydirectinput.press('.')
			up2-=1
			sleep(0.1)
		while up3 != 0:
			pydirectinput.press('/')
			up3-=1
			sleep(0.1)
		pyautogui.click(location[0], location[1])

