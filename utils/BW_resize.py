import os
import cv2
path = 'Z:/DATA/BW/2/'
save_path = 'Z:/DATA/BW/22/'
if not os.path.exists(save_path):
    os.makedirs(save_path)
imgs = os.listdir(path)
for i in imgs:
    img = cv2.imread(path+i)
    img = cv2.resize(img,(181,217))
    cv2.imwrite(save_path+i,img)


