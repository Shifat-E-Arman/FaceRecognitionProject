import cv2
import os

images = os.listdir('image_database/')

os.mkdir('image_database/Resized')    
couldnot=[]
count = 0
for x in range(84):
    img = cv2.imread('image_database/'+images[x],cv2.IMREAD_UNCHANGED)
    try:
        newimg = cv2.resize(img, (226,226) , interpolation=cv2.INTER_AREA)
        count = count+1
        cv2.imwrite('image_database/Resized/'+images[x],newimg)    
    
    except:
        print("Could not Resize ", images[x])
        couldnot.append(images[x])
        
    print(images[x])
    
    
print(count)
#newfile = open('error.txt','w')
#newfile.write(couldnot)
#newfile.close()





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
