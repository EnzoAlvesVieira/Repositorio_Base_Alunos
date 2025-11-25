import pyautogui as pg
from time import sleep
#pg.mouseInfo()
pg.press('win')
pg.write('Chrome', interval=0.2)
pg.press('enter')
sleep(1)
pg.write('github.com/EnzoAlvesVieira', interval=0.2)
pg.press('enter')