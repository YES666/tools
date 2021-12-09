##随机划分训练集、验证集、测试集
import os
import cv2
import random

n = 0
path = 'C:/Users/502/Desktop/ATLAS-SPECT1/'
save_path = 'C:/Users/502/Desktop/ATLAS-SPECT/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

path1 = path+'1/'
path2 = path+'2/'
save_path1 = save_path+'1/'
save_path2 = save_path+'2/'
def read_save(save_path1,save_path2,img_dir,n):
    if not os.path.exists(save_path1):
        os.makedirs(save_path1)
    if not os.path.exists(save_path2):
        os.makedirs(save_path2)
    for img_name in img_dir:
        img1 = cv2.imread(path1+img_name,0)
        img2 = cv2.imread(path2+img_name) 
        cv2.imwrite(save_path1+str(n).zfill(3)+'.png',img1)
        cv2.imwrite(save_path2+str(n).zfill(3)+'.png',img2)
        n+=1
    return n


img_dir = os.listdir(path1)
num = len(img_dir)
random.shuffle(img_dir)
read_save(save_path1+'train/',save_path2+'train/',img_dir[:8*num//10],n)
read_save(save_path1+'valid/',save_path2+'valid/',img_dir[8*num//10:9*num//10],n)
read_save(save_path1+'test/',save_path2+'test/',img_dir[9*num//10:],n)







