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
p=Pool(4)
def check_palindromic(str):
    result = True
    for i in range(len(str)/2+1):
        if str[i]<>str(len(str)-1-i):
            result = False
            break
    return result
def find_palindromic(str):
    ch_list=list('abcdefghijklmnlopqrstuvwxyz')
    ch_dict_list = [(x,[]) for x in ch_list]
    ch_dict = dict(ch_dict_list)
    for (i,x) in enumerate(str):
        ch_dict[x].append(i)
    for x in ch_dict:
        for index in ch_dict[x]:
            for index

