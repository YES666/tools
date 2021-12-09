import cv2
import os
import random
import numpy as np


def input_setup(image_size,stride,path1,save_path1,path2,save_path2):
    """
    Read image files and make their sub-images 
    """
 
    # Load data path
    data=os.listdir(path1)
    for i in range(len(data)):
        img1 = cv2.imread(path1+data[i],0)
        img2 = cv2.imread(path2+data[i],0)
        
        
        img11 = cv2.resize(img1,(128,128))
        img22 = cv2.resize(img2,(128,128))
        # img11 = img1
        # img22 = img2
        h,w = img11.shape
        x = random.randint(-30,30)
        y = random.randint(-30,30)
        M = np.float32([[1,0,x],[0,1,y]])
        img1_ = cv2.warpAffine(img11,M,(w,h))
        img2_ = cv2.warpAffine(img22,M,(w,h))

        cv2.imwrite(save_path1+str(i)+'.png',img11)
        cv2.imwrite(save_path2+str(i)+'.png',img22)
        cv2.imwrite(save_path1+str(i)+'_.png',img1_)
        cv2.imwrite(save_path2+str(i)+'_.png',img2_)
        if len(img1.shape) == 3:
            h, w, _ = img1.shape
        else:
            h, w = img1.shape
        #按14步长采样小patch
        for x in range(0, h-image_size+1, stride):
            for y in range(0, w-image_size+1, stride):
                sub_img1 = img1[x:x+image_size, y:y+image_size] # [33 x 33]
                cv2.imwrite(save_path1+str(i)+'_'+str(x)+'_'+str(y)+'.png',sub_img1)
                sub_img2 = img2[x:x+image_size, y:y+image_size] # [33 x 33]
                cv2.imwrite(save_path2+str(i)+'_'+str(x)+'_'+str(y)+'.png',sub_img2)

# def arg(save_path1,save_path2):
#     data=os.listdir(save_path1)
#     for i in range(len(data)):
#         img1 = cv2.imread(save_path1+data[i],0)
#         img2 = cv2.imread(save_path2+data[i],0)
#         h,w = img1.shape
#         x = random.randint(-30,30)
#         y = random.randint(-30,30)
#         M = np.float32([[1,0,x],[0,1,y]])
#         img1 = cv2.warpAffine(img1,M,(h,w))
#         img2 = cv2.warpAffine(img2,M,(h,w))
#         cv2.imwrite(save_path1+'/'+str(i)+'_.png',img1)
#         cv2.imwrite(save_path2+'/'+str(i)+'_.png',img2)



path1 = 'C:/Users/502/Desktop/ATLAS-SPECT/1/train/'
save_path1 = 'C:/Users/502/Desktop/ATLAS-SPECT/1/train_/'
path2 = 'C:/Users/502/Desktop/ATLAS-SPECT/2/train/'
save_path2 = 'C:/Users/502/Desktop/ATLAS-SPECT/2/train_/'
if not os.path.exists(save_path1):
    os.makedirs(save_path1)
if not os.path.exists(save_path2):
    os.makedirs(save_path2)
input_setup(128,32,path1,save_path1,path2,save_path2)