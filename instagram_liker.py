import time
import asyncio
import cv2
import numpy as np
import pyautogui as pag

screenWidth, screenHeight = pag.size()
print("Screen Width: ", screenWidth)
print("Screen Height: ", screenHeight)

def capture_region(x1, y1, x2, y2):
    img = pag.screenshot(region=(x1,y1,x2,y2))
    # For debugging, uncomment the following
    # img.save("captured_region.png")
    return img

def get_image_location(template_img_name, search_img, method):
    search_img_rgb = np.array(search_img)
    search_img_gray = cv2.cvtColor(search_img_rgb, cv2.COLOR_BGR2GRAY)
    template_img = cv2.imread(template_img_name, 0)
    res = cv2.matchTemplate(search_img_gray, template_img, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_loc

def like_photo():
	# Weird behavior for pixel width of capturing region vs moving mouse w/ pyautogui
	im = capture_region(0, (screenHeight*2)/6, screenWidth*2, screenHeight*2) 

	# If you want to compare template matching methods
	'''
	methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 
		'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
	for method in methods:
		mth = eval(method)
		location = get_image_location("likebutton.png", im, mth)
		print(location[0], location[1])
		pag.moveTo(location[0]/2, location[1]/2)
	'''

	location = get_image_location("likebutton.png", im, cv2.TM_CCOEFF) # cv2.TM_CCOEFF method works well 
	if (location[0] != 0):
		print(location[0], location[1])
		pag.moveTo(location[0]/2+20, location[1]/2+10+(screenHeight)/6) #divide by 2 bc pyautogui has weird res issues

def open_chrome():
	pag.hotkey('command', 'space')
	time.sleep(.4)
	pag.typewrite(['c', 'h', 'r', 'o', 'm', 'e', 'enter'], interval=.01)
	time.sleep(1)

def open_instagram():
	pag.moveTo(310, 78)
	pag.click()
	time.sleep(.1)
	pag.hotkey('ctrl', 'a')
	time.sleep(1)
	pag.typewrite(['i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', 'enter'], interval=.01)
	time.sleep(3)

def like_n_photos(n):
	for i in range(n):
		pag.scroll(-25)
		time.sleep(1)
		like_photo()
		time.sleep(1)


if __name__ == "__main__":
	open_chrome()
	open_instagram()
	like_n_photos(10)