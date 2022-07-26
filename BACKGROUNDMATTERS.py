import cv2 
import time
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*'XVID')
video=cv2.Videovideoture(0)
ret, frame = video.read()
print(frame)
frame=cv2.resize(frame,(640,480))
output_file=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
video=cv2.Videovideoture(0)
time.sleep(2)
bg=0
for i in range (60):
    ret,bg=video.read()
bg=np.flip(bg,axis=1)
while(video.isOpened()):
    ret,img=video.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_black=np.array([104,153,70])
    u_black=np.array([30,30,0])
    mask=cv2.inRange(l_black,u_black)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask=cv2.morphologyEx(mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    res_2=cv2.bitwise_and(bg,bg,mask=mask)
    final_output=cv2.addWeighted(res_2,1,0)
    f=frame-res_2
    f=np.where(f==0,image,f)
    output_file.write(final_output)
    cv2.imshow('magic',final_output)
    cv2.waitKey(1)
video.release()
cv2.destroyAllWindows()