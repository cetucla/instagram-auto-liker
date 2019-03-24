import pyautogui as pag
import time
# from imagesearch import *
import asyncio

import cv2
import numpy as np

screenWidth, screenHeight = pag.size()

print("Screen Width: ", screenWidth)
print("Screen Height: ", screenHeight)

def capture_region(x1, y1, x2, y2):
    img = pag.screenshot(region=(x1,y1,x2,y2))
    # img.save("captured_region.png")
    return img

def get_image_location(template_img_name, search_img, method):
    search_img_rgb = np.array(search_img)
    search_img_gray = cv2.cvtColor(search_img_rgb, cv2.COLOR_BGR2GRAY)
    template_img = cv2.imread(template_img_name, 0)

    res = cv2.matchTemplate(search_img_gray, template_img, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_loc

    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # if max_val < .8:
    #     return [-1, -1]
    # return max_loc


async def open_chrome():
	pag.hotkey('command', 'space')
	await asyncio.sleep(.4)
	pag.typewrite(['c', 'h', 'r', 'o', 'm', 'e', 'enter'], interval=.01)
	await asyncio.sleep(1)

async def open_instagram():
	pag.moveTo(310, 78)
	pag.click()
	await asyncio.sleep(.1)
	pag.hotkey('ctrl', 'a')
	await asyncio.sleep(1)
	pag.typewrite(['i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', 'enter'], interval=.01)
	await asyncio.sleep(3)

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

	# cv2.TM_CCOEFF method works well 
	location = get_image_location("likebutton.png", im, cv2.TM_CCOEFF)
	if (location[0] != 0):
		print(location[0], location[1])
		pag.moveTo(location[0]/2+20, location[1]/2+10+(screenHeight)/6) #divide by 2 bc pyautogui has weird res issues

async def like_all(num):
	for i in range(num):
		pag.scroll(-30)
		await asyncio.sleep(1)
		like_photo()
		await asyncio.sleep(2)



if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(open_chrome())
	loop.run_until_complete(open_instagram())
	loop.run_until_complete(like_all(10))