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
classes = ['CT','MR','SPECT']
cc = list(itertools.combinations(classes, 2))


path_save = 'C:/Users/502/Desktop/ATLAS-MM/'

pathsave_1 = path_save+'1/'
pathsave_2 = path_save+'2/'
if not exists(pathsave_1):
    os.makedirs(pathsave_1)
if not exists(pathsave_2):
    os.makedirs(pathsave_2)
path = 'C:/Users/502/Desktop/NEW_ATLAS/'

def output_classes(path):
    img_class = []
    if exists(path+'PD'):
        img_class.append('PD/')
    if exists(path+'T1'):
        img_class.append('T1/') 
    if exists(path+'T2'):
        img_class.append('T2/')
    return img_class



def read_save(path1,path2,num):
    
    for img_name in os.listdir(path1):
        img1 = cv2.imread(path1+'/'+img_name)
        #print(path1+'/'+img_name)
        #print(img1)
        #print(img1.shape)
        img2 = cv2.imread(path2+'/'+img_name) 
        cv2.imwrite(pathsave_1+str(num)+'.png',img1)
        cv2.imwrite(pathsave_2+str(num)+'.png',img2)


        num+=1
    return num
        

num=0
for m in range(len(cc)):
    for i,patient in enumerate(os.listdir(path)):
        #print(patient)

        path_patient = path + patient+'/'

        if not 'MR' in cc[m]:
            path1 = path_patient+cc[m][0]
            path2 = path_patient+cc[m][1]
            if exists(path1) and exists(path2):
                #print(num)
                num = read_save(path1,path2,num)
        else:
            img_class = output_classes(path_patient)
            if cc[m][0]=='MR':
                path2 = path_patient+cc[m][1]
                if len(img_class) > 0:
                    for j in img_class:
                        path1 = path_patient+j
                        if exists(path1) and exists(path2):
                            num = read_save(path1,path2,num)
            else:
                path1 = path_patient+cc[m][0]
                if len(img_class) > 0:
                    for j in img_class:
                        path2 = path_patient+j
                        if exists(path1) and exists(path2):
                            num = read_save(path1,path2,num)

                
                
            
            
