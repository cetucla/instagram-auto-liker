import pyautogui as pag
import time
from imagesearch import *

screenWidth, screenHeight = pag.size()

print("Screen Width: ", screenWidth)
print("Screen Height: ", screenHeight)

def open_chrome():
	pag.hotkey('command', 'space')
	time.sleep(.1)
	pag.typewrite(['c', 'h', 'r', 'o', 'm', 'e', 'enter'], interval=.01)
	time.sleep(1)
	open_instagram()

def open_instagram():
	pag.moveTo(310, 78)
	pag.click()
	time.sleep(.1)
	pag.hotkey('ctrl', 'a')
	time.sleep(1)
	pag.typewrite(['i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', 'enter'], interval=.01)
	time.sleep(.1)

	pos = imagesearcharea("likebutton.png", 0, 210, 1680, 1050)
	if pos[0] != -1:
		print("position : ", pos[0], pos[1])
		pyautogui.moveTo(pos[0], pos[1])
	else:
		print("image not found")

def like_photos():
	pag.moveTo(400, 1025)
	for i in range(5):
		time.sleep(1)
		pag.scroll(-100)
		#pag.click()



if __name__ == "__main__":
	open_chrome()
	# like_photos()