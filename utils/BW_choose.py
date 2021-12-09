# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#顺序是CT-T1-T2-PD-SPECT
import os
import cv2
import itertools
from os.path import exists
#import numpy as np
#classes = ['CT','MR']
#cc = list(itertools.combinations(classes, 2))


path_save = 'C:/Users/502/Desktop/BRAINWEB/'

pathsave_1 = path_save+'1/'
pathsave_2 = path_save+'2/'
if not exists(pathsave_1):
    os.makedirs(pathsave_1)
if not exists(pathsave_2):
    os.makedirs(pathsave_2)
path = 'C:/Users/502/Desktop/BrainWeb/'

def output_classes(path):
    img_class = []
    if exists(path+'PD'):
        img_class.append('PD/')
    # elif exists(path+'mr_PD'):
    #     img_class.append('mr_PD/')
    if exists(path+'T1'):
        img_class.append('T1/')
    # elif exists(path+'mr_T1'):
    #     img_class.append('mr_T1/')
    if exists(path+'T2'):
        img_class.append('T2/')
    # elif exists(path+'mr_T2'):
    #     img_class.append('mr_T2/')
    return img_class



def read_save(path1,path2,num):
    
    for i,img_name in enumerate(os.listdir(path1)):
        img1 = cv2.imread(path1+'/'+img_name,0)
        #img1 = cv2.resize(img1,(256,256))
        #print(path1+'/'+img_name)
        #print(img1)
        #print(img1.shape)
        img2 = cv2.imread(path2+'/'+os.listdir(path2)[i],0) 
        #img2 = cv2.resize(img2,(256,256))
        cv2.imwrite(pathsave_1+str(num)+'.png',img1)
        cv2.imwrite(pathsave_2+str(num)+'.png',img2)


        num+=1
    return num
def rename(path):
    for img_name in os.listdir(path):
        os.rename(path+img_name,path+img_name.split('.')[0].zfill(3)+'.jpg')


num=0
img_class = output_classes(path)
#print(img_class)
for i in range(3):
    path1 = path+img_class[i]
    for j in range(len(img_class)):
        if j>i:
            path2 = path+img_class[j]
            if exists(path1) and exists(path2):
                rename(path1)
                rename(path2)
                num = read_save(path1,path2,num)

        

            
                
            
            
