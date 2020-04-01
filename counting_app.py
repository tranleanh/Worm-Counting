# Tran Le Anh, 2020
# Dept. of Electronics Engineering
# Myongji University

import cv2
import numpy as np
import matplotlib.pyplot as plt

def count_contours(img):

	cnts, h = cv2.findContours(img, 1, 2)
	cnts = np.asarray(cnts)
	
	return cnts.shape[0]

def closing_process(img, kernel_size = 5):
	
	c_kernel = np.ones((kernel_size, kernel_size), np.uint8)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, c_kernel)
	
	return closing

def main():

	img = cv2.imread(img_name, 0)
	edges = cv2.Canny(img, 50, 100)

	ret, thresh1 = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)

	processed_img = closing_process(thresh1)

	final_count = count_contours(processed_img) - 2

	print('Image: ', img_name)
	print('Number of Worms: ', final_count)

	plt.subplot(121),plt.imshow(img, cmap = 'gray')
	plt.title('Image: ' + img_name), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(thresh1, cmap = 'gray')
	plt.title('Number of Worms: ' + str(final_count)), plt.xticks([]), plt.yticks([])
	
	plt.show()

if __name__ == '__main__':
	
# ===================================== #
	# CHANGE IMAGE FILE NAME HERE! #

	# img_name = 'worm_4_cropped.jpg'
	img_name = 'images/78.jpg'

# ===================================== #

	main()
