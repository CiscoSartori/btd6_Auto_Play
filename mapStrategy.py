import argparse
import json
from time import sleep
import datetime
import pyautogui
import pydirectinput
from function import Function

map_list = ['monkey_meadow','tree_stump','town_center',
            'middle_of_the_road','one_two_tree',
            'scrapyard','cubism', 'the_cabin']
class MapStrategy:

    def strategy():
        selectedMap = Function.map_verify(map_list)
        print(selectedMap)
        print(map_list[selectedMap])

        if selectedMap == 4:
            MapStrategy.one_two_tree()











    def monkey_meadow():
        tower=[12,12]
        Function.place_tower('u', )
        
    def tree_stump():
        tower=[12,12]
        Function.place_tower('u', )

    def town_center():
        tower=[12,12]
        Function.place_tower('u', )

    def middle_of_the_road():
        tower=[12,12]
        Function.place_tower('u', )

    def one_two_tree():
        tower=[253,815]
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        Function.round_verify('10')
        print('chegou aqui')

    def scrapyard():
        tower=[12,12]
        Function.place_tower('u', )
            
    def cubism():
        tower=[12,12]
        Function.place_tower('u', )

    def the_cabin():
        tower=[12,12]
        Function.place_tower('u', )

    def cubism():
        tower=[12,12]
        Function.place_tower('u', )