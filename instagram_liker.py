import pyautogui as pag
import time
screenWidth, screenHeight = pag.size()

print("Screen Width: ", screenWidth)
print("Screen Height: ", screenHeight)

def open_firefox():
	pag.hotkey('command', 'space')
	time.sleep(.1)
	pag.typewrite(['c', 'h', 'r', 'o', 'm', 'e', 'enter'], interval=.01)
	time.sleep(1)

def open_instagram():
	pag.moveTo(310, 78)
	pag.click()
	time.sleep(.1)
	pag.hotkey('ctrl', 'a')
	time.sleep(.1)
	pag.typewrite(['backspace'])
	pag.typewrite(['i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', 'enter'], interval=.01)
	time.sleep(.1)

def like_photos():
	pag.moveTo(400, 1025)
	for i in range(5):
		time.sleep(1)
		pag.scroll(-100)
		#pag.click()



if __name__ == "__main__":
	open_firefox()
	open_instagram()
	like_photos()