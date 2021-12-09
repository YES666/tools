#import cv2
#import os
import numpy as np
#from torchvision import transforms
#from PIL import Image

# path1 = 'C:/Users/502/Desktop/000.png'
# path2 = 'C:/Users/502/Desktop/000.png'
# img1 = cv2.imread(path1,0)
# img2 = cv2.imread(path2,0)
# #img1 = Image.open(path)
# #print(img)
# img = np.concatenate((img1[:,:,None],img2[:,:,None],img2[:,:,None]),axis=-1)
# print(img.shape)
# transform=transforms.Compose([
#     #transforms.Resize(256), #缩放图片，保持长宽比不变，最短边的长为224像素,
#     #transforms.ToTensor(),
#     transforms.ToPILImage(),
#     #transforms.Normalize((0.5,), (0.5,)) #将图片转换为Tensor,归一化至[0,1]
#     transforms.RandomHorizontalFlip(p=1),
#     transforms.RandomVerticalFlip(p=1),
#     #transforms.RandomRotation(180,resample=False,expand=False,center=None),
#     transforms.ToTensor()
# ])
# cv2.imwrite('C:/Users/502/Desktop/0.png',img)

# img = transform(img)
# print(img.shape)
# print(list(img.shape))
r = 1
region = np.arange(-r, r + 1, 1)
size = np.square(len(region))
[xs, ys] = np.meshgrid(region, region)
xs = xs.reshape(size, order='F')
ys = ys.reshape(size, order='F')
mid = (len(xs) - 1) // 2
x = np.delete(xs, mid)
y = np.delete(ys, mid)
