import cv2
import os
import uuid

# define a camera object
cam = cv2.VideoCapture(0) 

# names of the four unique objects that I will be using for data
img_names = ["StanleyCup"]
img_path = os.path.join('DataCollection', 'CaptureData', 'ObjectPhotos')
 
# This will create 5 photos for each object when I press the spacebar.
for img_name in img_names:
    if not os.path.exists(os.path.join(img_path, img_name)):
        os.mkdir(os.path.join(img_path, img_name)) 
    img_counter = 1  
    while (img_counter <= 25):
        ret, frame = cam.read() 
        # Display the resulting frame 
        cv2.imshow('frame', frame)  
        k = cv2.waitKey(1)   
        if k%256 == 32:
            # The space key was pressed 
            img_file_name = img_name + '.' + '{}.png'.format(str(uuid.uuid1()))
            path = f"./DataCollection/CaptureData/ObjectPhotos/{img_name}"
            cv2.imwrite(os.path.join(path, img_file_name), frame)
            print(f"{img_counter} {img_file_name} written!")
            img_counter += 1

# After the loop release the cap object 
cam.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 