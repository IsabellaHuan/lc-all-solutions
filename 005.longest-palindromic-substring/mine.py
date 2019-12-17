#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/16 下午5:32
# file : mine
"""
NOTICE:
寻找最长的对称子串
1、暴力，所有子串，去掉非对称子串
2、缩小候选集:即所有重复字符串为首尾的子串
确认是否区分大小写？是否有符号等
"""
from multiprocessing import Pool
import numpy as np
from itertools import product
p=Pool(4)
def check_palindromic(center_index,list):#如果从零元素开始
    result=True
    if (len(list)==1 and list[0]==1.0)\
            or(len(list)==1 and list[0]==center_index-int(center_index)==0.5): # 只有一个元素的情况下[注意特殊情况】
        redius=1
        return (result,redius)
    else:
        list0=list[0:-1]
        list1=list[1:]
        diff = np.array(list1)-np.array(list0)
        # print('diff',diff)
        invalid_diff = [(index,diff_i) for (index,diff_i) in enumerate(diff) if diff_i!=1.0]
        # print('invalid_diff',invalid_diff)
        if len(invalid_diff)==0:
            redius=len(list)
        else:
            redius = invalid_diff[0][0]# 第一个非零的索引即为连续的数量
        if redius==0:
            result=False
        return (result,redius)
def find_palindromic(str):
    ch_list=list('abcdefghijklmnlopqrstuvwxyz')
    ch_dict_list = [(x,[]) for x in ch_list]
    ch_dict = dict(ch_dict_list)
    for (i,x) in enumerate(str):
        ch_dict[x].append(i)
    ch_dict=dict(filter(lambda x:len(x[1])>1,ch_dict.items()))
    print(ch_dict)
    center_info={}
    for x in ch_dict:#通过中心来确定候选集合
        tmp=list(product(ch_dict[x],ch_dict[x]))
        candidate_pair = list(filter(lambda x:x[0]<x[1],tmp))
        # print('candidate_pair',candidate_pair)
        for pair in candidate_pair:
            center_type = (pair[0]+pair[1])%2 # 1,虚拟中心，0，实际中心
            center_index = (pair[0]+pair[1])*1.0/2
            ch_redius = (pair[1]-pair[0])*1.0/2
            if center_index in center_info:
                center_info[center_index].append(ch_redius)
            else:
                center_info[center_index]=[]
                center_info[center_index].append(ch_redius)
    print(center_info)
    for center_index in center_info:
        tmp=sorted(center_info[center_index])
        # print('tmp',tmp)
        (result,redius)=check_palindromic(center_index,tmp)
        # print(result,redius)
        if result:
            left_point = int(center_index-redius+center_index-int(center_index))
            right_point = int(center_index+redius-center_index+int(center_index))
            print(center_index,redius,str[left_point:right_point+1])

if __name__=='__main__':
    str = 'abcb'
    find_palindromic(str)
    str = 'abbe'
    find_palindromic(str)
    str = 'babad'
    find_palindromic(str)
    str = 'bccb'
    find_palindromic(str)
