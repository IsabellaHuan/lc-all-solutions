#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/16 下午2:12
# file : mine
"""
NOTICE:
1、列表没有排序
2、给出所有可能性
3、同一个元素只能用一次

->
1、暴力扫描，所有可能性都计算出来，然后比较target
2、既然是二者和，只要说明target与当前元素的差在输入列表中，说明就可以得到结果，为了查找方便，可以先进行排序
"""
# 排序保留索引值https://blog.csdn.net/li1367356/article/details/76439604
import numpy as np
def my_sort(input):
    sorted_input = np.sort(input)
    sorted_input_index = np.argsort(input)
    return sorted_input,sorted_input_index
def two_sum_target(input,target):
    [sorted_input,sorted_input_index] = my_sort(input)
    print sorted_input
    for (index,x) in enumerate(sorted_input[0:len(sorted_input)/2+1]):
        try:
            tmp_target = target - x
            pattern_index=list(sorted_input).index(tmp_target)
            print sorted_input_index[index],'=',x,sorted_input_index[pattern_index],'=',tmp_target
        except:
            print x,'no match'
            pass

if __name__=='__main__':
    input = [5,1,2,3,4,6,7,8,9]
    target = 13
    two_sum_target(input, target)


