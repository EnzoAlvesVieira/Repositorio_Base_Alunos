import pyautogui as pg
from time import sleep
#pg.mouseInfo()
pg.press('win')
pg.write('Chrome', interval=0.2)
pg.press('enter')
sleep(1)
pg.write('https://workspace.google.com/intl/pt-BR/gmail/', interval=0.1)
pg.press('enter')
pg.sleep(1)
pg.click(1667,114)