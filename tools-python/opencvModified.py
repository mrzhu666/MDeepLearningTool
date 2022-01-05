#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     : 2019/3/5 12:58
# @Author   : mr_zhu
# @Site     : 
# @project  : opencv
# @File     : cv2_modified.py
# @Software : PyCharm

import time
import cv2
import threading
import numpy as np

# 重载函数 加入fps显示功能
# 加入线程功能

class VideoCapture(cv2.VideoCapture):
    def __init__(self,*args,**kwargs):
        self._count=[]                              # 画面帧数
        self._count_detect = []                     # 检测帧数(算法)

        self.threading_current = False              # 线程正在运行
        self.threading_sucess_start = False

        super().__init__(*args,**kwargs)

    def add_fps_detect(self,img,count_n=20):
        self._count.append(time.time())
        if(len(self._count)>= 2):
            fps_current=count_n/(self._count[-1]-self._count[0])
            fps_text="fps: %.1f " % (fps_current)
            if (len(self._count_detect) >= 2):
                fps_current_detect = count_n / (self._count_detect[-1] - self._count_detect[0])
                fps_text += "fps_detect: %.1f " % (fps_current_detect)
                if(len(self._count_detect) > count_n):del self._count_detect[0]
            cv2.putText(img,fps_text,(40,self.frame.shape[0]-40),cv2.FONT_HERSHEY_SIMPLEX ,1,(255,255,255),2)
            if (len(self._count) >= count_n):del self._count[0]
        return img

    def detect_count(self):
        """
        检测时间添加
        :return:
        """
        self._count_detect.append(time.time())

    def thread(self,thread):
        if (not self.threading_current):
            t = threading.Thread(target=thread, args=(self,))
            # t.setDaemon(True)  # 设置为后台线程
            t.start()
            self.threading_current = True

    def thread_end(self):
        """
        添加检测时间点
        设置标志位
        :return:
        """
        self.detect_count()
        if (not self.threading_sucess_start): self.threading_sucess_start = True
        self.threading_current = False

def model(process,init=None,net="http://admin:admin@192.168.31.96:8082"):
    videocature=VideoCapture(net)
    cv2.namedWindow("video",cv2.WINDOW_NORMAL)
    # cv2.namedWindow("code", cv2.WINDOW_NORMAL)
    if init!=None:
        init()
    while True:
        res,videocature.frame=videocature.read()
        print(res)
        img=videocature.frame.copy()
        # videocature.thread(detect)

        # img=process(img)

        img = videocature.add_fps_detect(img)
        cv2.imshow("video",img)
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break
    videocature.release()
    cv2.destroyAllWindows()

def video_model():
    videocature=cv2_modified.VideoCapture("http://admin:admin@192.168.31.96:8082")
    cv2.namedWindow("video",cv2.WINDOW_NORMAL)

    while True:
        res,videocature.frame=videocature.read()
        img=videocature.frame.copy()
        # videocature.thread(detect)





        img = videocature.add_fps_detect(img)
        cv2.imshow("video",img)
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break
    videocature.release()
    cv2.destroyAllWindows()


def video_thread_model():
    def bbox(self):
        print('threading starts')



        print("threading ends")
        self.thread_end()

    videocature=cv2_modified.VideoCapture("http://admin:admin@192.168.31.96:8082")
    cv2.namedWindow("video",cv2.WINDOW_NORMAL)

    while True:
        res,videocature.frame=videocature.read()
        img=videocature.frame.copy()

        videocature.thread(bbox)


        img = videocature.add_fps_detect(img)
        cv2.imshow("video",img)
        if(cv2.waitKey(1) & 0xff == ord('q')):
            break
    videocature.release()
    cv2.destroyAllWindows()

def imageWindow(image:np.ndarray):
    """简单图片窗口生成，开启X11可以转送GUI窗口"""
    cv2.namedWindow("video",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("video", 640, 480)
    cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # 可调整窗口大小
    while True:

        cv2.imshow("video",image)
        if(cv2.waitKey(10) & 0xff == ord('q')):
            break
    cv2.destroyAllWindows()

if __name__=='__main__':
    model(process=None,net='http://admin:admin@192.168.1.248:8081')

# 1.coco.names 忘记调回
# videocature.thread(bbox)
# if(videocature.threading_sucess_start):
#                     for i in range(len(cap.boxes)):
#                         if(i<len(cap.boxes)):
#                             x0, y0, x1, y1 = cap.boxes[i]
#                             plot_one_box(cap.frame, [x0, y0, x1, y1], label=args.classes[cap.labels[i]], color=color_table[cap.labels[i]],score=cap.scores[i])
#                         cv2.putText(cap.frame, '{:.2f}ms'.format((cap.time_during) * 1000), (40, 40), 0,
#                                     fontScale=1, color=(0, 255, 0), thickness=2)

# def process(img):
#     return img
# model(process)