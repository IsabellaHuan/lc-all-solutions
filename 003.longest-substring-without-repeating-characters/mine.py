#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/16 下午3:19
# file : mine
"""
NOTICE:
暴力：所有子串，然后去掉存在重复字母的子串
高效做法：建立索引指针遇到重复的字母，则头指针跳到重复的最后的字母的下一位处，尾指针可以继续往下走
"""

def find_longest_substring(str):
    head_point=0
    tail_point=head_point+1
    longest_substring=''
    while head_point<len(str) and tail_point<len(str)+1: # 一直遍历到头指针指向最后一位或者尾指针超出字符串
        if tail_point<len(str) and str[tail_point] not in str[head_point:tail_point]:
            tail_point+=1
        elif tail_point==len(str): # 如果尾指针超过字符串，说明最后一个子串是不重复的，但是需要停止了
            longest_substring_candidate = str[head_point:tail_point]
            if len(longest_substring_candidate)>len(longest_substring):
                longest_substring=longest_substring_candidate
            break
        elif str[tail_point] in str[head_point:tail_point]:# 如果当前尾指针指向一个重复的字母，则调整头指针指向上一个重复字母的下一位，尾指针不动
            longest_substring_candidate = str[head_point:tail_point]
            if len(longest_substring_candidate) > len(longest_substring):
                longest_substring = longest_substring_candidate
            last_ch_index = tail_point-1-str[tail_point:0:-1].find(str[tail_point])# 获取上一个重复字母的索引
            head_point = last_ch_index + 1 # 头指针应该指向新字母前重复的最近的一个
            tail_point = tail_point # 尾指针不动
    return longest_substring

if __name__=='__main__':
    str='pwwkew'
    result = find_longest_substring(str)
    print result ,len(result)

