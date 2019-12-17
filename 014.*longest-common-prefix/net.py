#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/17 下午3:46
# file : net
"""
NOTICE:

"""
class Solution(object):
    def longestCommonPrefix(self,strs):
        '''

        :param strs: List[str]
        :return: str
        '''
        if not strs:
            return ''
        s1 = min(strs) # 按字母排序
        print('s1',s1)
        s2 = max(strs)
        print('s2', s2)
        for i,c in enumerate(s1):
            if c!= s2[i]:
                return s1[:i]
if __name__ == "__main__":
    s = Solution()
    print s.longestCommonPrefix(['flower','dog','car'])
    print s.longestCommonPrefix(['flower','flow','flight'])