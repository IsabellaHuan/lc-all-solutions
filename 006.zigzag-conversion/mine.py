#coding=utf-8
# author : huanshuwen
# time : 下午11:02
# file : mine
"""
NOTICE:
字母转置题
"""
import numpy
def convert(str):
    str_list=list(str)
    str_len = len(str)
    pooling_num = int(str_len/4)
    for times in range(pooling_num):
        str_list.insert(times * 6 + 3,'')
        str_list.insert(times * 6 + 5,'')
    print(str_list[0::6])
    print(str_list[1::3])
    print(str_list[2::6])
if __name__=='__main__':
    str='PAYPALISHIRING'
    convert(str)