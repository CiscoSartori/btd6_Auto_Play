import argparse
import json
from time import sleep
import datetime
import pyautogui
import pydirectinput
from function import Function

map_list = ['monkey_meadow','tree_stump','town_center',
            'middle_of_the_road','one_two_tree',
            'scrapyard','the_cabin',
            'resort','skates','lotus_island',
            'candy_falls','winter_park','carved',
            'park_path','alpine_run','frozen_over',
            'in_the_loop','cubism','four_circles',
            'hedge','end_of_the_road','logs']
class MapStrategy:

    def strategy():
        selectedMap = Function.map_verify(map_list)
        print(selectedMap)
        print(map_list[selectedMap])

        
        
        
        if selectedMap == 0:
            MapStrategy.monkey_meadow()
        if selectedMap == 1:
            MapStrategy.tree_stump()
        if selectedMap == 2:
            MapStrategy.town_center()
        if selectedMap == 3:
            MapStrategy.middle_of_the_road()
        if selectedMap == 4:
            MapStrategy.one_two_tree()
        if selectedMap == 5:
            MapStrategy.scrapyard()
        if selectedMap == 6:
            MapStrategy.the_cabin()
        if selectedMap == 7:
            MapStrategy.resort()
        if selectedMap == 8:
            MapStrategy.skates()
        if selectedMap == 9:
            MapStrategy.lotus_island()
        if selectedMap == 10:
            MapStrategy.candy_falls()
        if selectedMap == 11:
            MapStrategy.winter_park()
        if selectedMap == 12:
            MapStrategy.carved()
        if selectedMap == 13:
            MapStrategy.park_path()
        if selectedMap == 14:
            MapStrategy.alpine_run()
        if selectedMap == 15:
            MapStrategy.frozen_over()
        if selectedMap == 16:
            MapStrategy.in_the_loop()
        if selectedMap == 17:
            MapStrategy.cubism()
        if selectedMap == 18:
            MapStrategy.four_circles()
        if selectedMap == 19:
            MapStrategy.hedge()
        if selectedMap == 20:
            MapStrategy.end_of_the_road()
        if selectedMap == 21:
            MapStrategy.logs()
        




    def monkey_meadow():
        tower=[634,526]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        tack_shooter=[730,538]
        Function.place_tower('r',tack_shooter)
        Function.upgrade_tower(2,0,3,tack_shooter)
        round=Function.round_verify(20,round)
        ice=[835,835]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        alchemist=[919,543]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=1
        round=Function.round_verify(30,round)
        village=[690,709]
        Function.place_tower('k',village)
        Function.upgrade_tower(1,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(0,0,1,tack_shooter)
        round=Function.round_verify(37,round)
        Function.upgrade_tower(0,0,1,tack_shooter)

    def tree_stump():
        tower=[526,381]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        wizard=[712,402]
        Function.place_tower('a',wizard)
        Function.upgrade_tower(0,2,2,wizard)
        round-=1
        round=Function.round_verify(20,round)
        ice=[1327,456]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        round+=1
        round=Function.round_verify(30,round)
        village=[1411,363]
        Function.place_tower('k',village)
        Function.upgrade_tower(0,2,0,village)
        round=Function.round_verify(37,round)
        spike=[1052,727]
        Function.place_tower('j',spike)
        Function.upgrade_tower(3,2,0,spike)

    def town_center():
        tower=[661,153]
        round=0
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def middle_of_the_road():
        tower=[661,153]
        round=0
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def one_two_tree():
        tower=[245,820]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        ice=[1409,400]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        round=Function.round_verify(20,round)
        tack_shooter=[480,404]
        Function.place_tower('r',tack_shooter)
        Function.upgrade_tower(2,0,3,tack_shooter)
        alchemist=[507,244]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=2
        round=Function.round_verify(30,round)
        village=[1220,254]
        Function.place_tower('k',village)
        Function.upgrade_tower(1,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(0,0,1,tack_shooter)
        round=Function.round_verify(37,round)
        Function.upgrade_tower(2,0,0,alchemist)

    def scrapyard():
        tower=[661,153]
        round=0
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def the_cabin():
        tower=[661,153]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        ice=[477,956]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        round=-1
        round=Function.round_verify(20,round)
        buccaneer=[947,301]
        Function.place_tower('c',buccaneer)
        Function.upgrade_tower(2,2,0,buccaneer)
        round=Function.round_verify(30,round)
        village=[567,796]
        Function.place_tower('k',village)
        Function.upgrade_tower(2,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(1,0,0,buccaneer)
    
    def resort():
        tower=[661,153]
        round=0
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def skates():
        tower=[661,153]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)


    def lotus_island():
        tower=[1311,890]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(11,round)
        buccaneer=[754,781]
        Function.place_tower('c',buccaneer)
        Function.upgrade_tower(2,2,0,buccaneer)
        round-=1
        round=Function.round_verify(20,round)
        ice=[1203,159]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        round+=1
        round=Function.round_verify(30,round)
        village=[1257,298]
        Function.place_tower('k',village)
        Function.upgrade_tower(0,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(1,0,0,buccaneer)
        round=Function.round_verify(37,round)
        Function.upgrade_tower(1,0,0,buccaneer)

    def candy_falls():
        tower=[245,820]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        
    def winter_park():
        tower=[393,249]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        dart=[548,392]
        Function.place_tower('q',dart)
        Function.upgrade_tower(0,2,3,dart)
        round-=1
        round=Function.round_verify(20,round)
        ice=[1276,252]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        alchemist=[624,558]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=1
        round=Function.round_verify(30,round)
        village=[1282,408]
        Function.place_tower('k',village)
        Function.upgrade_tower(1,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(0,0,1,dart)
        round=Function.round_verify(37,round)
        Function.upgrade_tower(0,0,1,dart)

    def carved():
        tower=[245,820]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def park_path():
        tower=[245,820]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def alpine_run():
        tower=[517,806]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        # round=Function.round_verify(10,round)
        sleep(90)
        dart=[763,623]
        Function.place_tower('q',dart)
        Function.upgrade_tower(0,2,3,dart)
        round-=1
        # round=Function.round_verify(20,round)
        sleep(90)
        ice=[1123,674]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        alchemist=[685,479]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=1
        # round=Function.round_verify(30,round)
        sleep(60)
        village=[971,587]
        Function.place_tower('k',village)
        Function.upgrade_tower(2,2,0,village)
        # round=Function.round_verify(35,round)
        sleep(40)
        Function.upgrade_tower(0,0,1,dart)
        # round=Function.round_verify(37,round)
        sleep(5)
        Function.upgrade_tower(1,0,0,alchemist)

    def frozen_over():
        tower=[670,531]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        tack_shooter=[507,901]
        Function.place_tower('r',tack_shooter)
        Function.upgrade_tower(2,0,3,tack_shooter)
        round-=1
        round=Function.round_verify(20,round)
        ice=[1395,494]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        alchemist=[364,976]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=1
        round=Function.round_verify(30,round)
        village=[1369,626]
        Function.place_tower('k',village)
        Function.upgrade_tower(0,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(0,0,1,tack_shooter)
        round=Function.round_verify(37,round)
        Function.upgrade_tower(0,0,1,tack_shooter)

    def in_the_loop():
        tower=[245,820]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def cubism():
        tower=[661,153]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def four_circles():
        tower=[661,153]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def hedge():
        tower=[661,153]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def end_of_the_road():
        tower=[661,153]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)

    def logs():
        tower=[480,712]
        round=1
        Function.place_tower('u',tower)
        pydirectinput.press('space')
        pydirectinput.press('space')
        round=Function.round_verify(10,round)
        tack_shooter=[644,708]
        Function.place_tower('r',tack_shooter)
        Function.upgrade_tower(2,0,3,tack_shooter)
        round-=1
        round=Function.round_verify(20,round)
        ice=[1186,709]
        Function.place_tower('t',ice)
        Function.upgrade_tower(0,2,2,ice)
        alchemist=[822,713]
        Function.place_tower('f',alchemist)
        Function.upgrade_tower(2,2,0,alchemist)
        round+=1
        round=Function.round_verify(30,round)
        village=[1029,703]
        Function.place_tower('k',village)
        Function.upgrade_tower(0,2,0,village)
        round=Function.round_verify(35,round)
        Function.upgrade_tower(0,0,1,tack_shooter)
        round=Function.round_verify(37,round)
        Function.upgrade_tower(0,0,1,tack_shooter)
