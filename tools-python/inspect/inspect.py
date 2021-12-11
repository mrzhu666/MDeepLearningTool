import os
import math
import mailbox

def execCmd(cmd:str):
  """
  执行命令返回输出
  """
  r = os.popen(cmd)
  text = r.read()
  r.close()
  return text


def nvidia()->str:
  """
  返回N卡占用率
  """
  strN=execCmd("nvidia-smi")
  return strN


def main():
  string=nvidia().split('\n')
  print(*string,sep='\n')
  print(string[9][60:63])
  print(string[13][60:63])

if __name__=='__main__':
  main()
