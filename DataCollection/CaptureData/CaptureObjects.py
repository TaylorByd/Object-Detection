import cv2
import os

# define a camera object
cam = cv2.VideoCapture(0) 

# names of the four unique objects that I will be using for data
img_names = ["object1", "object2", "object3", "object4"]

# This will create 5 photos for each object when I press the spacebar.
for img_name in img_names:
    img_counter = 1  
    while (img_counter <= 5):
        ret, frame = cam.read() 

        # Display the resulting frame 
        cv2.imshow('frame', frame)  

        k = cv2.waitKey(1)   
        if k%256 == 32: 
            # The space key was pressed 
            img_file_name = f"{img_name}_{img_counter}.png"
            path = f"./DataCollection/CaptureData/ObjectPhotos/{img_name}"
            cv2.imwrite(os.path.join(path, img_file_name), frame)
            print("{} written!".format(img_file_name))
            img_counter += 1

# After the loop release the cap object 
cam.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 