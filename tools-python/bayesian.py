#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time     : 2019/4/14 16:56
# @Author   : mr_zhu
# @Site     : 
# @project  : TopView一
# @File     : bayesian.py
# @Software : PyCharm


import pandas as pd
import numpy as np

## notebook 库里引用其它库，被引用库修改了要重新加载
int_=['n_estimators','max_depth','min_samples_split','min_samples_leaf','max_features',
'max_leaf_nodes','num_leaves','min_samples_split','bootstrap','bagging_freq','lambda_l2','cat_smooth']

def result_report(res,method='continuous'):
    data_result = pd.DataFrame(res)

    data_result.sort_values(by='target', ascending=False, inplace=True)
    # if method=='continuous':
    #     return data_result['params'].iloc[0]
    # elif method=='discrete':
    data_set = {}
    for i, ii in data_result['params'].iloc[0].items():
        if i == 'bootstrap':
            data_set[i] = round(ii)
        elif i in int_:
            data_set[i] = int(ii)
        else:
            data_set[i] = ii
    print("训练集",data_result['target'].iloc[0])
    return data_set

def int_set(para):
    for i in para.keys():
        if i in int_:
            para[i]=int(para[i])
    return para