#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/17 下午7:57
# file : mine
"""
NOTICE:
生成回文
"""
class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.generateParenthesisIter('',n, n)
        return self.res

    def generateParenthesisIter(self, mstr, r_num, l_num):
        if r_num ==0 and l_num==0:
            self.res.append(mstr)
        if l_num>0:
            self.generateParenthesisIter(mstr+'(',r_num,l_num-1)#当前位置加左括号后遍历所有可能性
        if r_num>0 and r_num>l_num:
            self.generateParenthesisIter(mstr+')',r_num-1,l_num)#当前位置加有括号后遍历所有可能性
if __name__=='__main__':
    s=Solution()
    print s.generateParenthesis(3)