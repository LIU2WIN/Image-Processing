'''
Image_Procressing_Assignment_1
Bingkai Liu
104802173
'''

#import  libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read 'lena.tiff' and convert it to grayscale 
img = cv2.imread("lena.tiff", 0)

#mean filtering
Mean_3 = cv2.blur(img, (3,3))                      #window size is 3 
Mean_5 = cv2.blur(img, (5,5))                      #window size is 5

 #median  filtering
MedianResult_3 = cv2.medianBlur(img,3)
MedianResult_5 = cv2.medianBlur(img,5)

#plot and save images
titles=['Original','Mean_3','Mean_5','Median_3','Median_5']
images=[img,Mean_3,Mean_5,MedianResult_3,MedianResult_5]
for i in range(1,2,3,5,6):
       plt.subplot(2,3,i+2),plt.imshow(images[i],'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
plt.show()

