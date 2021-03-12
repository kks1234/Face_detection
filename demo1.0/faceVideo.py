import cv2
import tkinter as tk
from tkinter import filedialog#文件控件
#from PIL import Image, ImageTk#图像控件
import threading#多线程
from tkinter import *
import os
import time
import _thread
from threading import Thread
#root = tk.Toplevel()


import tkinter as tk 
from PIL import Image, ImageTk 
from itertools import cycle 

# 调用摄像头摄像头
cap = cv2.VideoCapture(0)


from tkinter import ttk

root = tk.Tk()
root.withdraw()
#win.geometry("600x600")


# 检测人脸
def detect_face(sample_image):
    # OpenCV 人脸检测
    face_patterns_people = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces_people = face_patterns_people.detectMultiScale(sample_image, scaleFactor=1.15, minNeighbors=5)
    return faces_people



# 圣诞帽
hats = []
for i in range(4):
    hats.append(cv2.imread('img/hat%d.png' % i, -1))

hat=hats[0]
# 显示人脸轮廓
def showFace(faces, sample_image):
    for x, y, w, h in faces:
        cv2.rectangle(sample_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return sample_image



# 戴帽子
def inHat(faces, sample_image,space1 , space2):
    global hat
    for face in faces:
        # 随机一顶帽子
        # hat = random.choice(hats)
       # hat = hats[3]
        # 调整帽子尺寸
        scale = face[3] / hat.shape[0] * 1.2
        hat = cv2.resize(hat, (0, 0), fx=scale, fy=scale)
        # 根据人脸坐标调整帽子位置
        x_offset = int(face[0] + face[2] / 2 - hat.shape[1] / 2 + space1)
        y_offset = int(face[1] - hat.shape[0] / 2  + space2)
        # 计算贴图位置，注意防止超出边界的情况
        x1, x2 = max(x_offset, 0), min(x_offset + hat.shape[1], sample_image.shape[1])
        y1, y2 = max(y_offset, 0), min(y_offset + hat.shape[0], sample_image.shape[0])
        hat_x1 = max(0, -x_offset)
        hat_x2 = hat_x1 + x2 - x1
        hat_y1 = max(0, -y_offset)
        hat_y2 = hat_y1 + y2 - y1
        # 透明部分的处理
        alpha_h = hat[hat_y1:hat_y2, hat_x1:hat_x2, 3] / 255
        alpha = 1 - alpha_h
        # 按3个通道合并图片
        for c in range(0, 3):
            sample_image[y1:y2, x1:x2, c] = (
                        alpha_h * hat[hat_y1:hat_y2, hat_x1:hat_x2, c] + alpha * sample_image[y1:y2, x1:x2, c])


def face_dect():
    # 调用摄像头摄像头
    cap = cv2.VideoCapture(0)
   
    while True:
        key = cv2.waitKey(1) & 0xFF
        ret, frame = cap.read()
        faces_people = detect_face(frame)
        # showFace(faces_people,frame)
        inHat(faces_people, frame)
        # 展示图片
    
        cv2.imshow("input", frame)
        # 监听用户案件
        if key == ord('q'):
            break
      
    
    cv2.destroyAllWindows()




a=1

def work2():
        # 调用摄像头摄像头
    global a
    cap = cv2.VideoCapture(0)
    space1 = 0
    space2 = 0
    while True:
        key = cv2.waitKey(1) & 0xFF
        ret, frame = cap.read()
        faces_people = detect_face(frame)
        # showFace(faces_people,frame)
        inHat(faces_people, frame, space1 , space2)
        # 展示图片
        font=cv2.FONT_HERSHEY_SIMPLEX#使用默认字体
        frame=cv2.putText(frame,'q: quit',(0,40),font,1.2,(255,0,0),2)#添加文字，1.2表示字体大小，（0,40）是初始的位置，(255,255,255)表示颜色，2表示粗细
        frame=cv2.putText(frame,'u: right',(0,80),font,1.2,(255,0,0),2)
        frame=cv2.putText(frame,'i: left',(0,120),font,1.2,(255,0,0),2)
        frame=cv2.putText(frame,'o: down',(0,160),font,1.2,(255,0,0),2)
        frame=cv2.putText(frame,'p: up',(0,200),font,1.2,(255,0,0),2)
        cv2.imshow("input", frame)
        # 监听用户案件
        if key == ord('u'):
            space1 += 10
        elif key == ord('i'):
            space1 -= 10
        elif key == ord('o'):
            space2 += 10
        elif key == ord('p'):
            space2 -= 10
        elif key == ord('q'):
            break
    cv2.destroyAllWindows()

def main():

    
    
   
    t2 = Thread(target=work2)
    t2.start()

    root = tk.Toplevel()
 
    def say_hi1():
           global hat
           hat=cv2.imread('img/hat0.png', -1)
    def say_hi2():
           global hat
           hat=cv2.imread('img/hat1.png', -1)
    def say_hi3():
           global hat
           hat=cv2.imread('img/hat2.png', -1)
    def say_hi4():
           global hat
           hat=cv2.imread('img/hat3.png', -1)
    def say_hi5():
           global hat
           hat=cv2.imread('img/hat4.png', -1)
    def say_hi6():
           global hat
           hat=cv2.imread('img/hat5.png', -1)
    def say_hi7():
           global hat
           hat=cv2.imread('img/hat6.png', -1)
    def say_hi8():
           global hat
           hat=cv2.imread('img/hat7.png', -1)
    def say_hi9():
           global hat
           hat=cv2.imread('img/hat8.png', -1)
    def say_hi10():
           global hat
           hat=cv2.imread('img/hat9.png', -1)
    def say_hi11():
           global hat
           hat=cv2.imread('img/hat10.png', -1)
    def say_hi12():
           global hat
           hat=cv2.imread('img/hat11.png', -1)


          
  
    photo = Image.open("img/hat0.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img0 = ImageTk.PhotoImage(photo)
    
    photo = Image.open("img/hat1.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img1 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat2.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img2 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat3.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img3 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat4.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img4 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat5.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img5 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat6.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img6 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat7.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img7 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat8.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img8 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat9.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img9 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat10.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img10 = ImageTk.PhotoImage(photo)
    photo = Image.open("img/hat11.png")  #括号里为需要显示在图形化界面里的图片
    photo = photo.resize((80,80))  #规定图片大小
    img11 = ImageTk.PhotoImage(photo)
    
    Button(root, image=img0,command=say_hi1).grid(row=0,column=0,columnspan=1, pady=1)
    Button(root, image=img1,command=say_hi2).grid(row=0,column=1,columnspan=1, pady=1)
    Button(root, image=img2,command=say_hi3).grid(row=0,column=2,columnspan=1, pady=1)
    Button(root, image=img3,command=say_hi4).grid(row=0,column=3,columnspan=1, pady=1)
    Button(root, image=img4,command=say_hi5).grid(row=1,column=0,columnspan=1, pady=1)
    Button(root, image=img5,command=say_hi6).grid(row=1,column=1,columnspan=1, pady=1)
    Button(root, image=img6,command=say_hi7).grid(row=1,column=2,columnspan=1, pady=1)
    Button(root, image=img7,command=say_hi8).grid(row=1,column=3,columnspan=1, pady=1)
    Button(root, image=img8,command=say_hi9).grid(row=2,column=0,columnspan=1, pady=1)
    Button(root, image=img9,command=say_hi10).grid(row=2,column=1,columnspan=1, pady=1)
    Button(root, image=img10,command=say_hi11).grid(row=2,column=2,columnspan=1, pady=1)
    Button(root, image=img11,command=say_hi12).grid(row=2,column=3,columnspan=1, pady=1)
    
    
    
    
    
    
    tk.mainloop()

if __name__ == "__main__":
    main()



























