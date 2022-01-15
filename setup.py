import os
import sys


print(os.system('ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk \'{print $2}\'|tr -d "addr:"'))
print(os.system('echo "$USER"'))  # 这样运行只有返回码

result=os.popen('echo "$USER"')
user=result.read().strip()



def import_moudle():
    """激活某个环境运行此脚本，添加模块路径，weishen
    """    
    source=sys.path[0]
    # source=os.path.dirname(__file__)
    print("当前工程文件夹路径："+source)
    for path in sys.path:  # 含有site-packages的路径为当前环境路径
        p=path.replace('/','\\')
        p=p.split('\\')
        if p[-1]=='site-packages':
            file_path=path
            break
    print('当前环境site-packages路径：'+path)
    file_path+='/custom.pth'

    if not os.path.exists(file_path):
        with open(file_path,mode='w') as f:
            f.write(source)
    else:
        with open(file_path,mode='r+') as f:
            content=f.readlines()
            print(content)
            if source not in content and source+'\n' not in content:
                f.write('\n'+source)


if __name__=='__main__':
    import_moudle()



