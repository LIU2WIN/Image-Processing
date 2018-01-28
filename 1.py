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
img= cv2.imread('lena.tiff',0)

#convert the image to binary format with threshold values of
#0.75, 0.5, 0.25, and 0.05
ret, threshold_075 = cv2.threshold(img,0.75*255,255,cv2.THRESH_BINARY)
ret, threshold_05 = cv2.threshold(img,0.5*255,255,cv2.THRESH_BINARY)
ret, threshold_025 = cv2.threshold(img,0.25*255,255,cv2.THRESH_BINARY)
ret,threshold_005 = cv2.threshold(img,0.05*255,255,cv2.THRESH_BINARY)

#name images
titles = ['Original','Threshold=0.75','Threshold=0.5','Threshold=0.25','Threshold=0.05']
images = [img,threshold_075,threshold_05,threshold_025,threshold_005]

#plot images
#question: if I use cv2.imshow() to display these images, l can get a fully white image when the threshold value is 0.05*255,
#but, if l use plt.imshow() to display these images, I get a fully black image. l can't figure it out.
for i in range (5):
       plt. subplot(2,3,i+1),plt.imshow(images[i],'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
plt.show()
##for i in range (5):
##       plt. subplot(2,3,i+1)
##       cv2.imshow(titles[i],images[i])            
##plt.show()
#generate the histogram of lena.tiff
Hist = cv2.calcHist([img],[0],None,[256],[0,256])
#process it with full scale histogram equalization
Equ = cv2.equalizeHist(img)
# plot the result of histogram equalization along the respective images and histogram 
plt.subplot(1,3,1),plt.plot(Hist,'gray')
plt.title('Histogram')
plt.subplot(1,3,2),plt.imshow(img,'gray')
plt.title('Orignal')
plt.subplot(1,3,3),plt.imshow(Equ,'gray')
plt.title('Equalization')
plt.show()


