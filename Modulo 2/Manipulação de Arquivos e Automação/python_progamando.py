import pyautogui as pg
from time import sleep
#pg.mouseInfo()
pg.press('win')
pg.write('Chrome', interval=0.2)
pg.press('enter')
sleep(1)
pg.write('Python online', interval=0.2)
pg.press('enter')
pg.click(919,394, duration=0.5)
