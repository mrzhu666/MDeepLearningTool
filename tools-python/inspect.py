import numpy as np
import os , re
def execCmd(cmd):
  r = os.popen(cmd)
  text = r.read()
  r.close()
  return text

# filepath='./oring_data/test_data/'
# fileList = os.listdir(filepath)
# for i in range(0,len(fileList)):
#     datapath=filepath+fileList[i]
#     result = execCmd('./teqc -relax'+datapath)
#     print(result)

print(execCmd("nvidia-smi"))