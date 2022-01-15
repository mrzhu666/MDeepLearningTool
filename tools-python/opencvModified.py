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
# 改进：时间记录列表改用循环数组

class VideoCapture(cv2.VideoCapture):
    def __init__(self,*args,**kwargs):
        self.n=20                                      # 平均数据点数
        self.count=[0]*self.n                              # 画面帧数
        self.count_detect = [0]*self.n                    # 检测帧数(算法)
        self.pointer=self.n-1                             # 视频流数据指针
        self.pointer_detect=self.n-1                     # 检测数据指针

        self.threading_current = False                     # 线程正在运行
        self.threading_sucess_start = False

        super().__init__(*args,**kwargs)

    def add_fps_detect(self,image)->np.ndarray:
        """添加帧数显示到画面中，

        Parameters
        ----------
        img : [type]
            [description]
        count_n : int, optional
            采用多少个数据取平均, by default 20

        Returns
        -------
        np.ndarray
            返回经过处理过的图像
        """        
        h,w=image.shape[:2]
        cv2.putText(image,"%dX%d"%(w,h),(image.shape[1]-200,20),cv2.FONT_HERSHEY_TRIPLEX ,0.7,(255,255,255),1)
        self.pointer=(self.pointer+1)%self.n
        self.count[self.pointer]=time.time()
        # self.count.append(time.time())
        if(self.count[(self.pointer+1)%self.n]!=0):  # 至少有n个数据点
            fps_current = self.n / (self.count[self.pointer]-self.count[(self.pointer+1)%self.n])
            fps_text="fps:%.1f " % (fps_current)
            if (self.count_detect[(self.pointer_detect+1)%self.n]!=0):  # 至少有n个数据点
                fps_current_detect = self.n / (self.count_detect[self.pointer_detect]-self.count_detect[(self.pointer_detect+1)%self.n])
                fps_text += "fpsD:%.1f" % (fps_current_detect)
            cv2.putText(image,fps_text,(8,image.shape[0]-20),cv2.FONT_HERSHEY_TRIPLEX ,0.7,(255,255,255),1)
        return image

    def detect_count(self):
        """检测时间点添加。在调用完算法检测后添加时间点
        """
        self.pointer_detect=(self.pointer_detect+1)%self.n
        self.count_detect[self.pointer_detect]=time.time()

    def thread(self,thread):
        if (not self.threading_current):
            t = threading.Thread(target=thread, args=(self,))
            # t.setDaemon(True)  # 设置为后台线程
            t.start()
            self.threading_current = True

    def thread_end(self):
        """添加检测时间点\n
        设置标志位
        """
        self.detect_count()
        if (not self.threading_sucess_start): self.threading_sucess_start = True
        self.threading_current = False

def model(init=None,net="http://admin:admin@192.168.137.9:8081"):
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

        # img = videocature.add_fps_detect(img)
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
    model()

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