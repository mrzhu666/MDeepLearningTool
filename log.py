#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:
    Used to keep a training logging
@Date       :2021/03/20 16:08:47
@Author     :xia
@version    :1.0
'''
import logging 
import time
import os

class Train_Logging():
    """
        @description:
            初始化时会写入一个回车和一行时间
            import sys
            sys.path.append(r'D:\zhu\pycharm\CADA-VAE-PyTorch-master\model_generate')
            import log
            example:
                第一次初始化:
                tlog=log.Train_Logging(path+filename)
                tlog.print_time()
                tlog.print(string)
                其它位置:
                tlog=log.Train_Logging()
                tlog.print(string)
    """
    def __init__(self,file_path='',file_mode='a'):
        """
            @description:
                具有全局性，初始化成功后，运行过程中basicConfig无法重新修改
                默认loggings文件夹
                example:
                    第一次初始化:
                    tlog=log.Train_Logging(path+filename)
                    tlog.print_time()
                    tlog.print(string)
                    其它位置:
                    tlog=log.Train_Logging()
                    tlog.print(string)
            ---------
            @param:
                file_path:文件路径名字，包括log后缀
                file_mode: 'w'重写
                        'a'续写
            -------
            @Returns:
            
            -------
        """
        file_path=file_path.replace('\\','/')
        if file_path:
            folder_path=file_path.split('/')
            folder_path='/'.join(folder_path[:-1])
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
        else:
            file_path='./loggings/temporary.log'
            if not os.path.exists('./loggings'):
                os.mkdir('./loggings')

        logging.basicConfig(level=logging.DEBUG,  
            # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', 
            format='%(message)s', 
            # datefmt='%a, %d %b %Y %H:%M:%S',
            filename=file_path,
            filemode=file_mode)

    def print(self,string='',display=True,**kwargs):
        logging.debug(string)
        if display:
            print(string,**kwargs)
    
    def print_time(self):
        self.ctime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.print('['+self.ctime+']')

if __name__=='__main__':
    log=Train_Logging('./loggings/test.log')
    log.print()
    log.print_time()
    log.print()

