# A Package Tool for Deep Learning

## Usage

- 

## Anaconda3

### 功能

添加路径调用全局自定义库文件

mymodule.pth 储存本文件夹路径，复制到site-packages文件夹

**Win10**

Anaconda3\Lib\site-packages 
Anaconda3\envs\xx\Lib\site-packages  

**Linux**

anaconda3/lib/python3.6/site-packages
anaconda3/lib/envs/xx/python3.6/site-packages

运行 `python setup.py` 为环境添加库

pip install -r requirements.txt

conda install --yes --file requirements.txt

## 已开发功能

- 训练过程和对应参数记录输出到日记
- 支持跨文件

## 待开发功能

- 参数注释注解记录

## 注意事项

开发过程注意保留原接口



