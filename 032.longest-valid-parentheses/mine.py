#coding=utf-8
# author: Huan Shuwen
# time : 2019/12/19 下午8:15
# file : mine
"""
NOTICE:
最长的有效括号组合
"""
class Solution(object):
  def longestValidParentheses(self, s):
      print(len(s))
      max_len=0
      head=0
      while head<len(s):
          if s[head]=='(':
              tail = head+1
              while tail<len(s):
                  if ((tail-head)%2==1 and s[tail]==')') or ((tail-head)%2==0 and s[tail]=='('):
                      tail +=1
                  else:
                      break
              s_len = tail - head
              if s_len%2==1:
                  s_len = s_len -1
               # tail指向第一个不进入有效子串的index
              max_len = max(max_len,s_len)
              print(head,tail,s[head:tail],max_len)
              head = tail
          else:
              head=head+1
      return max_len

if __name__=='__main__':
    s=Solution()
    print s.longestValidParentheses(')()())')
