import os
import cv2

def read_save(path,save_path):
    img = cv2.imread(path,0)
    cv2.imwrite(save_path,img)
def read_save1(path,save_path):
    img = cv2.imread(path)
    cv2.imwrite(save_path,img)

method = ['LP-SR','PC-LP','NSST-PAPCNN','Densefuse','VIFNet','IFCNN','Nestfuse','U2Fusion','FDAS']
dataset = 'SPECT'
index = '046'


save_path = 'C:/Users/502/Desktop/RESULT/CHOOSE/'+dataset+'/'
path = 'C:/Users/502/Desktop/RESULT/'
path1 = 'Z:/DATA/'+dataset+'/1/test_/'
path2 = 'Z:/DATA/'+dataset+'/2/test1/'

read_save(path1+index+'.png', save_path+index+'_1.png')
read_save1(path2+index+'.png', save_path+index+'_2.png')


for i in range(len(method)):
    #print(path+method[i]+'/'+index+'.png')
    if method[i] == 'FDAS':
        read_save1(path+method[i]+'/'+dataset+'1/train/'+index+'.png', save_path+index+'_'+str(i+3)+'.png')
    else:
        read_save1(path+method[i]+'/'+dataset+'1/'+index+'.png', save_path+index+'_'+str(i+3)+'.png')
    





