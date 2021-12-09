import cv2
import os
import random
import numpy as np

def rotate(img1,img2,h,w):
    angle = random.randint(-180,180)
    matRotate = cv2.getRotationMatrix2D((h*0.5, w*0.5), angle, 1)
    return cv2.warpAffine(img1, matRotate, (w,h)),cv2.warpAffine(img2, matRotate, (w,h))
def translation(img1,img2,h,w):
    x = random.randint(-30,30)
    y = random.randint(-30,30)
    M = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img1,M,(w,h)),cv2.warpAffine(img2,M,(w,h))

def reversal(img1,img2):
    k = random.randint(-1,1)
    return cv2.flip(img1,k),cv2.flip(img2,k)

path1 = 'C:/Users/502/Desktop/ATLAS-SPECT/1/test/'
save_path1 = 'C:/Users/502/Desktop/ATLAS-SPECT/1/test_/'
path2 = 'C:/Users/502/Desktop/ATLAS-SPECT/2/test/'
save_path2 = 'C:/Users/502/Desktop/ATLAS-SPECT/2/test_/'
if not os.path.exists(save_path1):
    os.makedirs(save_path1)
if not os.path.exists(save_path2):
    os.makedirs(save_path2)
data=os.listdir(path1)
for i in range(len(data)):
    img1 = cv2.imread(path1+data[i],0)
    img2 = cv2.imread(path2+data[i],0)
    cv2.imwrite(save_path1+str(i)+'.png',img1)
    cv2.imwrite(save_path2+str(i)+'.png',img2)
    h,w = img1.shape
    #resize
    img1_ = cv2.resize(img1,(128,128))
    img2_ = cv2.resize(img2,(128,128))
    cv2.imwrite(save_path1+str(i)+'_1.png',img1_)
    cv2.imwrite(save_path2+str(i)+'_1.png',img2_)
    
    #平移
    img11,img22 = translation(img1,img2,h,w)
    cv2.imwrite(save_path1+str(i)+'_2.png',img11)
    cv2.imwrite(save_path2+str(i)+'_2.png',img22)
    #旋转

    img111,img222 = rotate(img1,img2,h,w)
    cv2.imwrite(save_path1+str(i)+'_3.png',img111)
    cv2.imwrite(save_path2+str(i)+'_3.png',img222)

    #翻转
    img1111,img2222 = reversal(img1,img2)
    cv2.imwrite(save_path1+str(i)+'_4.png',img1111)
    cv2.imwrite(save_path2+str(i)+'_4.png',img2222)