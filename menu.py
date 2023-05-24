import argparse
import json
from time import sleep
import datetime
import pyautogui
from function import Function
from mapStrategy import MapStrategy

class Menu:    
    def start():

        Function.locateClick('resources/event/play.png')
        sleep(1)
        bonus = pyautogui.locateCenterOnScreen('resources/event/bonus.png',confidence=0.7)
        while bonus == None:
            sleep(2)
            right = pyautogui.locateCenterOnScreen('resources/map/right.png',confidence=0.9)
            pyautogui.click(right.x, right.y)
            sleep(2)
            bonus = pyautogui.locateCenterOnScreen('resources/event/bonus.png',confidence=0.7)
        pyautogui.click(bonus.x, bonus.y)
        sleep(0.5)
        
        Function.locateClick('resources/difficulty/easy.png')

        Function.locateClick('resources/difficulty/play.png')
        sleep(5)

    def end():
        next = None
        while next == None:
            next = pyautogui.locateCenterOnScreen('resources/menu/next.png',confidence=0.9)
            sleep(1)
        Function.locateClick('resources/menu/next.png')
        sleep(0.1)
        Function.locateClick('resources/menu/home.png')
        sleep(1)
        if (pyautogui.locateCenterOnScreen('resources/event/collect.png',confidence=0.9)):
            Function.locateClick('resources/event/collect.png')
            sleep(0.3)
            Function.locateClick('resources/event/collect.png')



        sleep(0.5)

    def start2():

        Function.locateClick('resources/event/play.png')
        sleep(1)
        Function.locateClick('resources/map/left.png')
        
        Function.locateClick('resources/map2/dark_castle.png')
        # Function.locateClick('resources/map/'+mapa+'.png')
        
        
        Function.locateClick('resources/difficulty/hard.png')

        Function.locateClick('resources/difficulty/chimps.png')
        sleep(5)
	