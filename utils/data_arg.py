# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:30:19 2019

@author: 502
"""

from PIL import Image
import os
path = 'C:/Users/Administrator/Desktop/ATLAS1/'
save_path = 'C:/Users/Administrator/Desktop/ATLAS_aug/'
classes = ['CT/','MR/']

os.mkdir(save_path)
for i in classes:
    os.mkdir(os.path.join(save_path,i))


for i in classes:
    path1 = path +i
    imgs = os.listdir(path1)
    for m,img_name in enumerate(imgs):
        img = Image.open(path1+img_name)
        img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img2 =img.transpose(Image.FLIP_LEFT_RIGHT)
        img3 = img.transpose(Image.ROTATE_90)
        img4 = img.transpose(Image.ROTATE_180)
        img5 = img.transpose(Image.ROTATE_270)
        path2 = save_path +i
        img.save(path2+'image'+str(6*(m)+1)+'.jpg')
        img1.save(path2+'image'+str(6*(m)+2)+'.jpg')
        img2.save(path2+'image'+str(6*(m)+3)+'.jpg')
        img3.save(path2+'image'+str(6*(m)+4)+'.jpg')
        img4.save(path2+'image'+str(6*(m)+5)+'.jpg')
        img5.save(path2+'image'+str(6*(m)+6)+'.jpg')
        print('已保存'+str(6*(m)+6)+'张')

print('finish')