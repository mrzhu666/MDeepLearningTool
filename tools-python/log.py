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
        具有全局性，初始化成功后，运行过程中basicConfig无法重新修改
        初始化时会写入一个回车和一行时间
    @example:
        from log import tlog
        tlog.init(file_path)
        tlog.parameter=value
        tlog.print(string)
        tlog.print_time()
        tlog.print_parameter()
    """
    def __init__(self,file_path='',file_mode='a'):
        """[summary]

        Parameters
        ----------
        file_path : str, optional
            文件路径名字，包括log后缀, by default ''
        file_mode : str, optional
            'w'重写,'a'续写, by default 'a'
        """        
        self.non_para=['ctime','non_para','file_name']  # 存储类属性名称
        if file_path:
            self.init(file_path,file_mode)

    def init(self,file_path='',file_mode='a'):
        file_path=file_path.replace('\\','/')
        file_path=file_path.replace('//','/')
        self.file_name=file_path.split('/')[-1]
        if file_path:
            folder_path=file_path.split('/')
            folder_path='/'.join(folder_path[:-1])
            if not os.path.exists(folder_path):
                # os.mkdir(folder_path)
                os.makedirs(folder_path)
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
        ctime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.print('['+ctime+']')

    def print_note(self,string,file_name="deafult"):
        file_path="./logging/note/"+self.file_name
        folder_path=file_path.split('/')
        folder_path='/'.join(folder_path[:-1])
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        content=['\n','['+self.ctime+']\n',string+'\n']
        with open(file_path,mode='a') as f:
            f.writelines(content)
 

    def print_parameter(self):
        """
        打印输出参数
        """
        mini=10  # 每一行最少字符数
        parameter={i:j for i,j in self.__dict__.items() if i not in self.non_para}
        parameter=['']+[str(i)+'='+str(j) for i,j in parameter.items()]
        para_len=[len(i) for i in parameter]
        para_len=list(accumulate(para_len))
        l=0
        for r in range(1,len(parameter)):
            if para_len[r]-para_len[l]>7:
                self.print(','.join(parameter[l+1:r+1]))
                l=r
        if l<len(parameter)-1:
            self.print(','.join(parameter[l+1:]))

tlog=Train_Logging()

if __name__=='__main__':
    log=Train_Logging('./loggings/test.log')
    log.print()
    log.print_time()
    log.print()

