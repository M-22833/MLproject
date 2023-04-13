import cv2
import os
import numpy as np
import time

def sketch(photo):
    k = 7
    #Read Image
    img=cv2.imread(photo)
    #cv2.imread(img)
    # Convert to Gray Image
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(gray_img)
    invert_img=255-gray_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k,k),40,40)

    # Invert Blurred Image
    invert_blur_img=cv2.bitwise_not(blur_img)
    invert_blur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(gray_img,invert_blur_img, scale=255.0)

    # Save Sketch 
    #cv2.imwrite('sketch00000.jpg', sketch_img)

    # Display sketch"""
    #ret,sketch_bw = cv2.threshold(sketch_img,245,255,0)
    #cv2.imshow("sketched", sketch_img)
    #cv2.imshow("sketched_thresholded", sketch_bw)
    #display(sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return sketch_img


dir = "C:\\Users\\Manas\\PROJECTS\\ML project\\img_align_celeba\\face_imgs"
    
#image = cv2.imread(dir + '\\000001.jpg')

#Function call
#sketch(photo = dir + '\\000002.jpg')

for file in os.listdir(dir):
    if file.endswith("jpg"):
      cv2.imwrite("C:\\Users\\Manas\\PROJECTS\\ML project\\img_align_celeba\\face_sketches\\" + file, sketch(photo = dir + '\\' + file))
      print(file + "Added to face_sketches...")
