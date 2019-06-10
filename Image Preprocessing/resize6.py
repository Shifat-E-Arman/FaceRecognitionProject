import cv2
import os
import numpy as np
import pandas as pd

images = os.listdir('image_database/Resized')

#os.mkdir('image_database/Resized')    

for x in range(len(images)):
    
    if ".JPG" in images[x] or ".jpg" in images[x]:
        
        img = cv2.imread('image_database/Resized/'+images[x])
        gtimg = cv2.imread('image_database/ground_truth/'+images[x])
        
        img=np.array(img)
        var = img.shape[0]*img.shape[1]
        pixels = img.flatten()    
        
        b = np.transpose(pixels[:var])
        g = np.transpose(pixels[var:2*var])
        r = np.transpose(pixels[2*var:])
        
        gtimg = cv2.imread('image_database/ground_truth/'+images[x])
        gtimg=np.array(cv2.cvtColor(gtimg, cv2.COLOR_BGR2GRAY))
        gt = np.ndarray(shape=(gtimg.shape[0],gtimg.shape[1]),dtype=basestring)
        
        gt[gtimg>128] = "true"
        gt[gtimg<128] = "false"
        
        gtpixels = gt.flatten()    
        gtpixels = np.transpose(gtpixels)
        
        N=np.ndarray(shape=(var,3),dtype=int)
        
        N[:,0]=r
        N[:,1]=g
        N[:,2]=b
        #N[:,3]=gtpixels
        df = pd.DataFrame(data=N, index=None, columns=['red','green','blue'], copy=False)
        df['label']=gtpixels
        print("Storing ", images[x])
        with open('final_both.csv','a') as f:
            df.to_csv(f,index=False, header = False)
