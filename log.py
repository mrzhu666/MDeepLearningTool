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
from itertools import accumulate

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
        self.non_para=['ctime','non_para']
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

    def print_parameter(self):
        mini=20  # 每一行最少字符数
        parameter={i:j for i,j in self.__dict__.items() if i not in self.non_para}
        parameter=['']+[str(i)+'='+str(j) for i,j in parameter.items()]
        print(len(parameter))
        para_len=[len(i) for i in parameter]
        para_len=list(accumulate(para_len))
        l=0
        print(para_len)
        for r in range(1,len(parameter)):
            if para_len[r]-para_len[l]>7:
                self.print(','.join(parameter[l+1:r+1]))
                l=r
        if l<len(parameter)-1:
            self.print(','.join(parameter[l+1:]))


if __name__=='__main__':
    log=Train_Logging('./loggings/test.log')
    log.print()
    log.print_time()
    log.print()

