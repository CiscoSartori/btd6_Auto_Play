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
        if selectedMap == 7:
            MapStrategy.the_cabin()










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
        tower=[245,820]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        print('chegou aqui10', round)
        ice=[1409,400]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)

        round=Function.round_verify(20,round)
        print('chegou aqui20', round)
        tack_shooter=[480,404]
        Function.place_tower('r',tack_shooter)
        Function.upgrade_tower(2,0,3,tack_shooter)
        alchemist=[507,244]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=1
        round=Function.round_verify(30,round)
        print('chegou aqui30', round)
        village=[1220,254]
        Function.place_tower('k',village)
        Function.upgrade_tower(1,2,0,village)

        round=Function.round_verify(35,round)
        print('chegou aqui35', round)
        Function.upgrade_tower(0,0,1,tack_shooter)

    def scrapyard():
        tower=[12,12]
        Function.place_tower('u', )
            
    def cubism():
        tower=[12,12]
        Function.place_tower('u', )

    def the_cabin():
        tower=[661,153]
        round=0
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        print('chegou aqui10', round)
        ice=[477,956]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        round=Function.round_verify(20,round)
        buccaneer=[947,301]
        Function.place_tower('c',buccaneer)
        Function.upgrade_tower(2,2,0,buccaneer)
        print('chegou aqui20',round)
        round=Function.round_verify(30,round)
        village=[567,796]
        Function.place_tower('k',village)
        Function.upgrade_tower(2,2,0,village)
        print('chegou aqui30',round)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(1,0,0,buccaneer)
        print('chegou aqui35',round)

    def cubism():
        tower=[12,12]
        Function.place_tower('u', )