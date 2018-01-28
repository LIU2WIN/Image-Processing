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

#Sobel detector
x = cv2.Sobel(img,cv2.CV_16S,1,0)  
y = cv2.Sobel(img,cv2.CV_16S,0,1)

Sobel_X = cv2.convertScaleAbs(x)   
Sobel_Y = cv2.convertScaleAbs(y)
Result_Sobel =Sobel_X+Sobel_Y

#Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_gaussian = cv2.GaussianBlur(img,(3,3),0)
Prewitt_X = cv2.filter2D(img_gaussian, -1, kernelx)
Prewitt_Y = cv2.filter2D(img_gaussian, -1, kernely)
Result_Prewitt =Prewitt_X + Prewitt_Y
##Result_Prewitt = cv2.addWeighted(img_prewittx,0.5,img_prewitty,0.5,0)

#Laplacian detector
gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)  
Result_Laplacian = cv2.convertScaleAbs(gray_lap)




#plot and save images
titles=['Result_Sobel','Result_Prewitt','Result_Laplacian']
images=[Result_Sobel,Result_Prewitt,Result_Laplacian]
for i in range(3):
       plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
       plt.title(titles[i])
       plt.xticks([]),plt.yticks([])
plt.show()



