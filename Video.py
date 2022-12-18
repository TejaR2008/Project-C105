import os
import cv2
from PIL import Image


path = "Images"
images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)            
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)

output = cv2.VideoWriter("Project.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)
for i in range (0, count - 1):
    img = cv2.imread(images[i])
    #cv2.imshow("window", img)
    output.write(img)

print(frame.shape)