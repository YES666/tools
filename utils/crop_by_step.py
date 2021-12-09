import cv2
import os

def input_setup(path,image_size,stride,save_path):
    """
    Read image files and make their sub-images 
    """
 
    # Load data path
    data=[os.path.join(path,k) for k in os.listdir(path)]


    for i in range(len(data)):
        img = cv2.imread(data[i])
        if len(img.shape) == 3:
            h, w, _ = img.shape
        else:
            h, w = img.shape
        #按14步长采样小patch
        for x in range(0, h-image_size+1, stride):
            for y in range(0, w-image_size+1, stride):
                sub_img = img[x:x+image_size, y:y+image_size] # [33 x 33]
                cv2.imwrite(save_path+'/'+str(i)+'_'+str(x)+'_'+str(y)+'.png',sub_img)

                            
path = 'Z:/DATA/BW/2'
save_path = 'Z:/DATA/BW_/2'
if not os.path.exists(save_path):
    os.makedirs(save_path)
input_setup(path,128,32,save_path)