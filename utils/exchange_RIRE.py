# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:19:32 2020

@author: Adminstrator
"""
#转换
import pydicom
import scipy.misc
import os

path = 'C:/Users/Administrator/Desktop/RIRE_DATA/'
save_path = 'C:/Users/Administrator/Desktop/DATA/'
for patient in os.listdir(path):
    patient_path = path+patient+'/'
    for i in os.listdir(patient_path):
        os.makedirs(save_path+patient+'/'+i+'/')
        for a,j in enumerate(os.listdir(patient_path+i)):
            img = pydicom.read_file(patient_path+i+'/'+j)
            img = img.pixel_array
            scipy.misc.imsave(save_path+patient+'/'+i+'/'+str(a)+'.jpg',img)