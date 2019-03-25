import pyautogui
import cv2
import numpy as np
import time
import sys

screenWidth, screenHeight = pyautogui.size()

def open_chrome():
	time.sleep(.5)
	pyautogui.hotkey('command', 'space')
	time.sleep(.5)
	pyautogui.typewrite(['s', 'a', 'f', 'a', 'r', 'i', 'enter'], interval=.1)
	time.sleep(1)

def full_screen():
	pyautogui.hotkey('ctrl', 'command', 'f')
	time.sleep(1)

def open_instagram(hashtag="default"):
	pyautogui.moveTo(700, 20)
	pyautogui.click()
	time.sleep(.1)
	pyautogui.hotkey('ctrl', 'a')
	time.sleep(1)
	if hashtag == "default":
		pyautogui.typewrite(['backspace', 'i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', '.', 'c', 'o', 'm', 'enter'], interval=.1)
	else:
		URL = ['backspace']
		prefix = "instagram.com/explore/tags/"
		for x in prefix:
			URL.append(x)
		for x in hashtag:
			URL.append(x)
		URL.append('/')
		URL.append('enter')
		pyautogui.typewrite(URL, interval=.1)
	time.sleep(5)

def like_personal():
	X_LEFT = 0
	X_RIGHT = screenWidth
	Y_TOP = 150
	Y_DOWN = screenHeight

	imag = pyautogui.screenshot(region=(X_LEFT, Y_TOP, X_RIGHT, Y_DOWN))
	imag.save("suckmyballs.png")
	img_rgb = cv2.imread('suckmyballs.png')
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	template = cv2.imread('icon.png', 0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.7
	loc = np.where( res >= threshold)

	if len(loc[0]) == 0 and len(loc[1]) == 0:
		pyautogui.scroll(-15)
		time.sleep(1)
		return
	else:
		for pt in zip(*loc[::-1]):
			xCoor = int(pt[0])
			yCoor = int(pt[1])
			cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

			pyautogui.moveTo(xCoor + 20, yCoor + Y_TOP + 20)
			time.sleep(0.4)
			pyautogui.click()
			time.sleep(0.4)
			pyautogui.scroll(-15)
			time.sleep(1)

	# cv2.imwrite('Detected.png',img_rgb)

def like_hashtag():
	X_LEFT = 0
	X_RIGHT = screenWidth
	Y_TOP = 150
	Y_DOWN = screenHeight

	imag = pyautogui.screenshot(region=(X_LEFT, Y_TOP, X_RIGHT, Y_DOWN))
	imag.save("suckmyballs.png")
	img_rgb = cv2.imread('suckmyballs.png')
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	template = cv2.imread('icon.png', 0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.7
	loc = np.where( res >= threshold)

	if len(loc[0]) == 0 and len(loc[1]) == 0:
		pyautogui.press('right')
		time.sleep(1)
		return
	else:
		for pt in zip(*loc[::-1]):
			xCoor = int(pt[0])
			yCoor = int(pt[1])
			cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

			pyautogui.moveTo(xCoor + 20, yCoor + Y_TOP + 20)
			time.sleep(0.4)
			pyautogui.click()
			time.sleep(0.4)
			pyautogui.press('right')
			time.sleep(1)

if __name__ == "__main__":
	startTime = time.time()
	open_chrome()
	full_screen()
	if len(sys.argv) > 1: # like a hashtag
		open_instagram(sys.argv[1])
		pyautogui.moveTo(390, 540)
		pyautogui.click()
		time.sleep(1)
		while 1:
			if time.time() - startTime > 1800:
				exit()
			like_hashtag()
	else: # like people you follow's photos
		open_instagram()
		pyautogui.moveTo(X_RIGHT - 50, Y_TOP + 50)
		pyautogui.click()
		time.sleep(0.5)
		while 1:
			if time.time() - startTime > 1800: 
				exit()
			like_personal()
