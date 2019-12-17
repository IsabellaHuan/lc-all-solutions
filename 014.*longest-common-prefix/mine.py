#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/17 下午2:43
# file : mine
"""
NOTICE:
匹配最长前缀
1、暴力，一个字母一个字母往后尝试
2、折半对比：以最短的字符串为基础，对比前半段，然后再折半
# 扩展，如果是最长子串呢？
"""
import numpy as np
def longest_prefix(list):
    shortest_str_index = np.argmin(map(lambda x:len(x),list))
    shortest_str=list[shortest_str_index]
    head_point = 0
    tail_point = len(shortest_str)/2+1
    max_tail_point = 0
    # 终止条件:
    while head_point<len(shortest_str) \
            and tail_point<len(shortest_str)\
            and head_point<tail_point\
            and max_tail_point<tail_point:
        candidate_str = shortest_str[head_point:tail_point]
        print('shortest_str', shortest_str)
        print('candidate_str',candidate_str)
        flag = True
        flag=(sum(map(lambda x:x[head_point:tail_point]==candidate_str,list))==len(list))
        if flag:#前半部分是，继续往后扩展
            current_max_tail_point = tail_point
            tail_point = tail_point+(len(shortest_str)-tail_point)/2+1
        else:#前半部分不是，则去掉后半段
            shortest_str = candidate_str
            tail_point = len(shortest_str)/2
    return shortest_str[head_point:tail_point]

if __name__=='__main__':
    list=['aaaaab','aaaaac','aaaaae','aaaaad','aaaaaf','aaaaag','aaaaah']
    print(longest_prefix(list))

