import cv2
import os
import numpy as np
import pandas as pd

images = os.listdir('image_database/ground_truth')
#os.mkdir('image_database/Resized')    

for x in range(len(images)):
    
    if ".JPG" in images[x] or ".jpg" in images[x]:
        
        gtimg = cv2.imread('image_database/ground_truth/'+images[x])
        gtimg=np.array(cv2.cvtColor(gtimg, cv2.COLOR_BGR2GRAY))
        gt = np.ndarray(shape=(gtimg.shape[0],gtimg.shape[1]),dtype=int)
        gt[gtimg>128] = 1
        gt[gtimg<128] = 0
    
        
        var = gtimg.shape[0]*gtimg.shape[1]
        gtpixels = gtimg.flatten()    
        
        N=np.ndarray(shape=(var,3),dtype=int)
        
        N[:,0]=r
        N[:,1]=g
        N[:,2]=b
        df = pd.DataFrame(data=N, index=None, columns=['red','green','blue'], copy=False)
        print("Storing ", images[x])
        with open('new.csv','a') as f:
            df.to_csv(f,index=False)


        
        
        
        
        
    