import os
import cv2
import numpy as np
import glob

def bgr2yuv(path,save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    imgs = os.listdir(path)
    for img_name in imgs:
        img_path = path+img_name
        img = cv2.imread(img_path)
        img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
        cv2.imwrite(save_path+img_name,img_yuv[:,:,0])


#path1是生成的单通道图像
#path2是原YUV图像
def yuv2bgr(path1,path2,save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    img_paths = glob.glob(path1+'*.png')
    imgs = [j.split('\\')[-1] for j in img_paths]
    print(imgs)
    for img_name in imgs:
        img_path1 = path1+img_name
        img1 = cv2.imread(img_path1)
        img1 = img1[:,:,0]
        img_path2 = path2+img_name
        img2 = cv2.imread(img_path2)
        result = cv2.cvtColor(np.concatenate((img1[:,:,None],img2[:,:,1:]),axis = -1),cv2.COLOR_YUV2BGR)
        cv2.imwrite(save_path+img_name,result)

def onechannel(path,save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    imgs = os.listdir(path)
    for img_name in imgs:
        img_path = path+img_name
        img = cv2.imread(img_path)
        #img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
        cv2.imwrite(save_path+img_name,img)


#path1 = 'Z:/DARTS/augments/train/'
path = 'C:/Users/502/Desktop/ATLAS-SPECT/2/valid/'
#path2 = 'Z:/DATA/ATLAS-SPECT/TEST/2/'

save_path = 'C:/Users/502/Desktop/ATLAS-SPECT/2/valid1/'
#onechannel(path,save_path)
bgr2yuv(path,save_path)
#yuv2bgr(path1,path2,save_path)
#yuv2bgr(path,path2,save_path)
#print((img[:,:,0]==img_yuv[:,:,0]).all())