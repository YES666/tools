import numpy as np

#打乱numpy数组
def shuffle_data(data,label,num):
    index = np.arange(num)
    np.random.shuffle(index)
    data= data[index]
    label = label[index]
    return data,label



import random

#打乱list
a = [j for j in range(len(image_path))]  
random.shuffle(a) 
for j in range(len(a)):
    image_path[j] = image_path[a[j]]
    label[j] = label[a[j]]
