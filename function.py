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
	

	def round_verify(img):
		round = None
		while round == None:
			round = pyautogui.locateCenterOnScreen('resources/round/'+img+'.png', confidence=0.9)
			print('round')
			sleep(3)
	
	def place_tower(tower_type, location):
		pydirectinput.press(tower_type)
		sleep(0.1)
		pyautogui.moveTo(location[0], location[1])
		sleep(0.1)
		pyautogui.click(location[0], location[1])
		sleep(0.2)




tower_types = {
	'hero': 'u',
	'dart_monkey': 'q',
	'boomerang_monkey': 'w',
	'bomb_shooter': 'e',
	'tack_shooter': 'r',
	'ice_monkey': 't',
	'glue_gunner': 'y',
	'sniper_monkey': 'z',
	'monkey_sub': 'x',
	'monkey_buccaneer': 'c',
	'monkey_ace': 'v',
	'heli_pilot': 'b',
	'mortar_monkey': 'n',
	'dartling_gunner': 'm',
	'wizard_monkey': 'a',
	'super_monkey': 's',
	'ninja_monkey': 'd',
	'alchemist': 'f',
	'druid': 'g',
	'banana_farm': 'h',
	'engineer_monkey': 'l',
	'spike_factory': 'j',
	'monkey_village': 'k'
}