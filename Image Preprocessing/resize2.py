import cv2
import os
import numpy as np
import pandas as pd

images = os.listdir('image_database/Resized')

#os.mkdir('image_database/Resized')    


img = np.array(cv2.imread('Roll01_left_b copy.JPG'))
print(img)

var = img.shape[0]*img.shape[0]

pixels = img.flatten()
b = np.transpose(pixels[:var])
g = np.transpose(pixels[var:2*var])
r = np.transpose(pixels[2*var:])

N=np.ndarray(shape=(var,3),dtype=int)

N[:,0]=r
N[:,1]=g
N[:,2]=b

x = pd.DataFrame(data=N, index=None, columns=['red','green','blue'], copy=False)
x.to_csv('new.csv')
print(x.head)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
