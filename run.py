import argparse
import json
from time import sleep
import datetime
import pyautogui
from function import Function
from mapStrategy import MapStrategy
from menu import Menu




for i in range(1000):
	Menu.start2()
	MapStrategy.strategy()
	Menu.end()
	print('done')