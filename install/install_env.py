import os
file = 'conda.txt'# 用于存储第三方库名称，从第一行开始写，用回车键分割。将该文本文档放在.py文件同一文件夹下。

with open(file,'r') as f:
    libs = f.readlines() # 读取文本文档中的每一行

web = "https://pypi.tuna.tsinghua.edu.cn/simple "# 清华大学镜像源。
# web = "http://mirrors.aliyun.com/pypi/simple "  # 阿里云镜像源。
# web = "https://pypi.mirrors.ustc.edu.cn/simple "  # 中国科技大学镜像源。
# web = "http://pypi.douban.com/simple "  # 豆瓣镜像源。

try:
    for lib in libs:
        lib=lib.rstrip("\n") # 去掉换行符 "\n"
        # os.system("pip3 install -i "+ web + lib) # 选择其中一个镜像源，下载安装库。
        os.system("conda install "+lib)
except:
	print("fail")