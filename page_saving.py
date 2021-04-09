import pyautogui as pag

#pag.hotkey('winleft', 'r')
pag.PAUSE = 5
print(pag.position())
pag.click(x=119,y=629)
pag.typewrite(['c','m','d','enter'])

pag.PAUSE = 0.5
pag.keyDown('winleft')
pag.press('r')
pag.keyUp('winleft')
pag.click(x=119,y=629)
pag.doubleClick()
pag.typewrite(['c','m','d','enter'])

pag.PAUSE = 0.5
pag.keyDown('winleft')
pag.press('r')
pag.keyUp('winleft')
pag.click(x=119,y=629)
pag.hotkey('ctrl', 'a')
pag.typewrite(['c','m','d','enter'])

# short Python 3 program that will constantly print out the position of the mouse cursor
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

loc = pag.locateOnScreen('help.png')
print(loc.left,loc.top,loc.width,loc.height)

loc = pag.locateCenterOnScreen('help.png')
pag.click(x=loc.x,y=loc.y)

loc = pag.locateOnScreen('help.png')
pag.center(loc)

import pyperclip
import time
loc= pag.locateOnScreen('chrome.png', confidence=0.9)
loc = pag.center(loc)
pag.click(x=loc.x,y=loc.y)
pag.press('right')
pag.press('right')
pag.press('right')
pag.press('enter')
loc= pyautogui.locateOnScreen('addressbar.png', confidence=0.7)
loc = pag.center(loc)
pag.click(x=loc.x,y=loc.y)
pag.write('https://www.facebook.com')
pag.press('enter')
time.sleep(10)
loc = pag.locateCenterOnScreen('myprofile.png')
pag.click(x=loc.x,y=loc.y)
time.sleep(10)
loc = pag.locateCenterOnScreen('friends.png')
pag.click(x=loc.x,y=loc.y)

loc = pag.locateCenterOnScreen('friends.png')
pag.click(x=loc.x,y=loc.y)

import pyperclip as pc
pc.copy('santo')
pc.paste()

import pyperclip
import time
loc= pyautogui.locateOnScreen('chrome.png', confidence=0.9)
loc = pag.center(loc)
pag.click(x=loc.x,y=loc.y)
pag.press('right')
pag.press('right')
pag.press('right')
pag.press('enter')
time.sleep(5)
loc = pag.locateCenterOnScreen('scrolldown.png')
while True:
    pag.click(x=loc.x,y=loc.y)

