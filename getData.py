import cv2
import numpy as np
import face_recognition as fr
import os
import time
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
print("Nhập tên : ")
name=input()
print("Start  :")
cap = cv2.VideoCapture(0)
count=1
try:
    while True:
        _, img = cap.read()# _true  or false . img: data lay dc 
        #img=cv2.imread(r"D:\FaceDetect\facend\face_rec\faces\vy4.png")
        face_locations = fr.face_locations(img)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# convent chuyen anh ve anh xam(du lieu anh,mauGRB(blue,red,green)->gray)
    # faces = face_cascade.detectMultiScale(gray,1.1,3)#nhan dien khuon mat 
        for (top, right, bottom, left) in face_locations: #x,y toa do diem tinh tien ngang doc
        # print(x,y,w,h)
            cv2.rectangle(img, (left-20, top-40), (right+20, bottom+20), (255, 0, 0), 2)
            img_drop=img[top:bottom,left:right]
            cv2.imshow('DETECTION FACE', img)
            if not os.path.exists(r"D:\FaceDetect\facend\hiii\Dataset/"+name):
                os.makedirs(r"D:\FaceDetect\facend\hiii\Dataset/"+name)
            cv2.imwrite(r"D:\FaceDetect\facend\hiii\Dataset/"+name+"/"+name+"."+str(count)+".jpg",img_drop)
            time.sleep(0.4)
            cv2.imshow("Face",img_drop)   
            count=count+1

        if count>10:
                break   
        k = cv2.waitKey(1) & 0xff==ord('q')  
        if(k):
             break
except:
    print("Khong tim thay khuon mat")
cap.release() # giai phong bo nho
cv2.destroyAllWindows()  # huy no đi
