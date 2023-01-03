import cv2
import os


input_path="/home/images"
os.chdir(input_path)
images=glob.glob("*.png")

for image in images:
    img=cv2.imread(img)
    width,length=img.shape[0:2]
    image = cv2.copyMakeBorder(src, top, bottom, left, right, borderType)
