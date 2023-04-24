# import the two modules
import cv2
import numpy as np
# load path of the image
original_image=cv2.imread("G:\FCAI\Third year\second semester\Image Proccessing\project\image.jpg")
cv2.imshow('original image',original_image)
cv2.waitKey(0)
# create a sharpening kernel
sharpen_filter=np.array([[-1,-1,-1],
                 [-1,9,-1],
                [-1,-1,-1]])
# applying kernels to the input image to get the sharpened image
sharp_image=cv2.filter2D(original_image,-1,sharpen_filter)
cv2.imshow('Required image',sharp_image)
cv2.waitKey(0)
cv2.destroyAllWindows()