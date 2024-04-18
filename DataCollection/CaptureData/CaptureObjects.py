import cv2
import os

# define a camera object
cam = cv2.VideoCapture(0) 

# names of the four unique objects that I will be using for data
img_names = ["object1", "object2", "object3", "object4"]

# variable used to access the img names
img_name_element = 0 

# This will create 5 photos for each object when I press the spacebar.
for i in range(4):
    img_counter = 1  
    while (img_counter <= 5):
        ret, frame = cam.read() 

        # Display the resulting frame 
        cv2.imshow('frame', frame) 

        k = cv2.waitKey(1) 
        if k%256 == 32: 
            # The space key was pressed
            img_name = f"{img_names[img_name_element]}_{img_counter}.png"
            path = f"./DataCollection/CaptureData/ObjectPhotos/{img_names[img_name_element]}"
            cv2.imwrite(os.path.join(path, img_name), frame)
            print("{} written!".format(img_name))
            img_counter += 1
    img_name_element += 1

# After the loop release the cap object 
cam.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 