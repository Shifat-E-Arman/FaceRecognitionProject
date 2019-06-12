import cv2
import os

images = os.listdir('image_database/resized')
for files in images:
    if ('jpg' not in files) or ('JPG' not in files):
        images.remove(files)
        
os.mkdir('image_database/resized/again')    
couldnot=[]
count = 0
for x in range(len(images)):
    img = cv2.imread('image_database/resized/'+images[x],cv2.IMREAD_UNCHANGED)
    
    try:
        newimg = cv2.resize(img, (28,28) , interpolation=cv2.INTER_AREA)
        count = count+1
        cv2.imwrite('image_database/resized/again/'+images[x],newimg)    
    
    except:
        print("Could not Resize ", images[x])
        couldnot.append(images[x])
        
    print(images[x])
        
    
print(count)
#newfile = open('error.txt','w')
#newfile.write(couldnot)
#newfile.close()





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
