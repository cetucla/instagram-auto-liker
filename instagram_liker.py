import pyautogui
import cv2
import numpy as np
import time

screenWidth, screenHeight = pyautogui.size()

print("Screen Width: ", screenWidth)
print("Screen Height: ", screenHeight)

def open_chrome():
	time.sleep(.5)
	pyautogui.hotkey('command', 'space')
	time.sleep(.5)
	pyautogui.typewrite(['s', 'a', 'f', 'a', 'r', 'i', 'enter'], interval=.1)
	time.sleep(1)

def full_screen():
	pyautogui.hotkey('ctrl', 'command', 'f')
	time.sleep(1)

def open_instagram():
	pyautogui.moveTo(700, 20)
	pyautogui.click()
	time.sleep(.1)
	pyautogui.hotkey('ctrl', 'a')
	time.sleep(1)
	pyautogui.typewrite(['backspace', 'i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', '.', 'c', 'o', 'm', 'enter'], interval=.1)
	time.sleep(3)

def findLikes():
	imag = pyautogui.screenshot(region=(0, 150, 1430, 898))
	imag.save("suckmyballs.png")
	img_rgb = cv2.imread('suckmyballs.png')
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	template = cv2.imread('icon.png', 0)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	threshold = 0.7
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		print("heart found at x : " + pt[0] + w + " and y : " + pt[1] + h)
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

	cv2.imwrite('Detected.png',img_rgb)

def like_photos():
	pyautogui.moveTo(400, 1025)
	for i in range(5):
		time.sleep(1)
		pyautogui.scroll(-100)
		#pyautogui.click()


if __name__ == "__main__":
	open_chrome()
	full_screen()
	open_instagram()
	findLikes()
	# like_photos()