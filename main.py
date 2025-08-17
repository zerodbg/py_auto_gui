
# For sleeping the program
import time

# For automating mouse work
import pyautogui
# to open chrome
click_1 = pyautogui.locateCenterOnScreen('click_1.png', confidence = 0.7)

pyautogui.moveTo(click_1)

pyautogui.doubleClick(click_1)

time.sleep(5)
# to click on search bar

pyautogui.write('https://www.youtube.com/')

pyautogui.hotkey('enter')

time.sleep(15)
#to click on yt search bar

click_3 = pyautogui.locateCenterOnScreen('click_3.png', confidence = 0.7)

pyautogui.moveTo(click_3)

pyautogui.click(click_3)

time.sleep(5)

pyautogui.write('GFX ELITE GAMING')

pyautogui.hotkey('enter')

time.sleep(5)

# to click on chanel logo

click_4 = pyautogui.locateCenterOnScreen('click_4.png', confidence = 0.7)

pyautogui.moveTo(click_4)

pyautogui.click(click_4)

time.sleep(8)

# to click on subscribe button
x=364
y=364
pyautogui.moveTo(364, 364)
pyautogui.click(x=364, y=495)
