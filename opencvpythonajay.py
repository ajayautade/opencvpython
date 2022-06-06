#Resize Image with python OpenCv library
''' Hi This Is a Code for Resizing Images Using The Pythons OpenCv Library 
    you can resize multiple images by just single code 
    Mention the size of image you want and make sure you past that images in the script folder
'''
import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    #mention the size of image below 
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    #It Will write the resized file name starting with resized_ajay.jpg likewise 
    cv2.imwrite("resized_"+image,re)
