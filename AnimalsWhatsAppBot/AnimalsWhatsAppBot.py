import pyautogui as pg
import time

time.sleep(10)

txt = open('C:\Projects\Python\AnimalsWhatsAppBot\\animals.txt', 'r')

a = "Ruben is a"

for i in txt:
    pg.write(a + ' ' + i)
    pg.press('Enter')