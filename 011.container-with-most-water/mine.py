#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/17 上午11:31
# file : mine
"""
NOTICE:
疑惑点：
必须是相邻的两个点吗？
容器是封口还是不封口呢？
"""
# 假设是不相邻的两个点；不封口；==>容器的体积为 j>i : min(ai,aj)*（j-i）
import numpy as np

def max_container(list):#list:[(i,ai)]
    sorted_list = sorted(list,key=lambda x:x[1])
    result_list = []
    for (index,(i,ai)) in enumerate(sorted_list[0:-1]):
        larger_list = sorted_list[index+1:]
        farrest_point_index = np.argmax(map(lambda x:abs(x[0]-i),larger_list))
        # print(farrest_point_index)
        farrest_point = (sorted_list[index+1:])[farrest_point_index]
        # print('farrest_point',farrest_point)
        result_list.append(((i,ai),farrest_point,ai*abs(farrest_point[0]-i)))
        # print('result_list', result_list)
    # print('final result_list',result_list)
    largest_index = np.argmax(map(lambda x:x[-1],result_list))
    return result_list[largest_index]
if __name__=='__main__':
    list=[(1,4),(2,2),(3,1),(4,5),(5,1)]
    print max_container(list)