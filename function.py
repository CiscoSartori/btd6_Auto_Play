import argparse
import json
from time import sleep
import datetime
import pyautogui





class Function:
	def locateClick(img):
		location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
		pyautogui.click(location.x, location.y)
		sleep(0.5)
	

	def map_verify(img):
		game_map = None
		while game_map == None


map_list = {
	
}
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