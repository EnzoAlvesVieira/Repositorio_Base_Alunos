import pyautogui as pg
from time import sleep
#pg.mouseInfo()
pg.press('win')
pg.write('Chrome', interval=0.2)
pg.press('enter')
sleep(1)
pg.write('www.youtube.com', interval=0.2)
pg.press('enter')
sleep(1)
pg.write(';', interval=0.2)
pg.write('wellington rato cortou pra esquerda narração', interval=0.2)
pg.press('enter')
pg.click(1068,350, duration=1)


